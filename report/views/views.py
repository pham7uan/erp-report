from django.http import HttpResponse
from django.shortcuts import render, redirect

from report import mrp2, data_30
from report.rest import *
import json
from report.mrp import *
from django.utils import timezone
from report.models import *
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from report.tests import *


@xframe_options_exempt
def synchronous_report_current(request):
    products = get_products()
    # print products
    # products = response['resutls']
    if request.method == 'POST':
        data ={}
        input={
            'product':request.POST['product'],
            'bom':request.POST['version'],
            'time':timezone.now(),
        }

        if request.POST['product'] == 'All':
            for p in products:
                boms = get_boms(p['id']).json()['resutls']
                data[p['id']] = []
                for bom in boms:
                    data[p['id']].append(bom['id'])
        else:
            product_id = request.POST['product']

            if request.POST['version'] == 'All':
                boms = get_boms(product_id).json()['resutls']
                data[product_id] = []
                for bom in boms:
                    data[product_id].append(bom['id'])
                # boms.append(bom)
            else:
                data[product_id] = []
                data[product_id].append(request.POST['version'])

        # print data
        result = {}
        for p_id, p_bom_ids in data.items():
            for p_bom_id in p_bom_ids:
                # print p_bom_id
                data = get_data(p_bom_id)
                bom = data['bom']
                materials= data['materials']
                # # print materials
                lp_vars = []
                A_eq = []
                B_eq = []
                B_ineq = []
                A_ineq = []
                objective = []
                materials_dict ={}
                max = calculator(bom,materials,lp_vars,A_eq,B_eq,A_ineq,B_ineq,objective,materials_dict)

                for key, value in materials_dict.items():
                    if '_' not in key:
                        materials_dict.pop(key, None)
                # materials_list ={}
                try:
                    materials_list = sorted(materials_dict.items(),key=lambda v: map(int, v[0].split("_")[1].split(".")))
                except:
                    materials_list = sorted(materials_dict.items(), key=lambda v: v[0].split("_")[1].split("."))
                p = filter(lambda p: p['id'] == int(p_id), products)[0]
                bom_list = get_boms(p_id).json()['resutls']
                b = filter(lambda b: b['id'] == int(p_bom_id), bom_list)[0]

                p_name = p['name'] +' - Bom: '+ b['name']
                result[p_name] = {'max':max,'materials_list':materials_list}
            # print result
        day = datetime.now().strftime('%Y-%m-%d')
        report_name = 'Bao cao dong bo - ' + day
        report = Report(name=report_name, input=input, result=result)
        report.save()
        return render(request, "synchronous_report.html", {'result': result,'input':input,'name':'synchronous_report_current'})
        # return render(request, "synchronous_report_current.html", {'products': products})
    if request.method == 'GET':
        reports = Report.objects.all()
        history={}
        for r in reports:
            history[r.id] = {'name':r.name, 'created':r.created}
        # print history
        return render(request, "synchronous_report_current.html",{'products':products, 'history':history})

@xframe_options_exempt
def synchronous_report(request,pk):
    if request.method == 'GET':
        r = Report.objects.get(pk=pk)
        print r.name
        print r.input
        print r.result
        return render(request, "synchronous_report.html", {'result': r.result,'input':r.input,'name':r.name})

@xframe_options_exempt
def save_report(request):
    if request.method == 'POST':
        print 'Save'
        report = Report(name = request.POST['name'],input =  request.POST['input'], result =request.POST['result'] )
        report.save()
        print request.POST['result']
    return render(request, "synchronous_report.html",{'result': report.result, 'input': report.result, 'name': report.result})

# @xframe_options_exempt
# def report_preview(request):
#     receive = hang_ve_test
#     production_plan = production_plan_test
#     return render(request,'report_preview.html',{'production_plan':production_plan,'receive':receive})

@csrf_exempt
def mrp_calculator(request):
    if request.method == 'POST':
        # print request.body
        json_data = json.loads(request.body.decode(encoding='UTF-8'))
        data = json_data['data']
        # data = data2.data
        bom = data['bom']
        materials = data['materials']
        lp_vars = []
        A_eq = []
        B_eq = []
        B_ineq = []
        A_ineq = []
        objective = []
        materials_dict = {}
        result = {}
        max = calculator(bom, materials, lp_vars, A_eq, B_eq, A_ineq, B_ineq, objective, materials_dict)
        if max ==0:
            minimum_condition = check_minimum(bom,materials,1)
            result['number'] = 0
            result['detail'] = minimum_condition

            return HttpResponse(json.dumps(result))
        for key, value in materials_dict.items():
            if '_' not in key:
                materials_dict.pop(key, None)
        #sort materials by level
        try:
            materials_list = sorted(materials_dict.items(), key=lambda v: map(int, v[0].split("_")[1].split(".")))
        except:
            materials_list = sorted(materials_dict.items(), key=lambda v: v[0].split("_")[1].split("."))


        detail =[]
        for m in materials_list:
            level = m[0].split('_')[1]
            name = m[0].split('_')[0]
            quantity = m[1],
            tmp = {
                level:{name:quantity}
            }
            detail.append(tmp)
        detail_json = json.dumps(detail)
        result = {
            'number':max,
            'detail':detail
        }
        result_json = json.dumps(result)
        return HttpResponse(result_json)
    return HttpResponse('Hello, this is mrp calculator api. Method POST, body: {"data":your_dict}')

@csrf_exempt
def mrp_calculator2(request):
    if request.method == 'POST':
        # print request.body
        # json_data = json.loads(request.body.decode(encoding='UTF-8'))
        # data = json_data['data']
        # data = data2.data
        mrp2.bom = data_30.data['bom']
        mrp2.materials = data_30.data['materials']
        result = mrp2.main()
        result_json = json.dumps(result)
        return HttpResponse(result_json)
    return HttpResponse('Hello, this is mrp calculator api. Method POST, body: {"data":your_dict}')


def check_minimum(bom, materials,required):
    check_result ={}
    for key, value in bom.iteritems():
        # print key
        sum =0
        min = value[1]*required
        for v in value[0]:
           sum = sum + int(materials[v])
        if sum < min:
            check_result[key] = [value[0],min-sum]
    # print check_result
    return check_result
    # result_json = json.dumps(check_result)

