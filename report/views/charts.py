from django.http import HttpResponse,Http404
from django.shortcuts import render, redirect
from report.rest import *
# import report.tests
from django.views.decorators.clickjacking import xframe_options_exempt
from report.utils import *
from report.tests import *

g_production=[]
g_plan ={}
g_year =2017


@xframe_options_exempt
def dashboard(request,year):
    try:
        # token = request.META['HTTP_TOKEN']
        token = "hsadj12312328"
        is_valid = True
        if is_valid:
            request.session['token'] = token
        else:
            raise Http404("You do not have permission")
    except:
        raise Http404("You do not have permission")

    global g_production
    global g_plan
    global g_year
    g_year = year
    g_plan = get_reality_production_detail(year)
    g_production = get_reality_production(year)

    # g_production = production_test
    # g_plan = production_plan_test
    if bool(g_production):
        return render(request,'dashboard.html',{'production':g_production,'production_plan':g_plan,'year':year})
    return HttpResponse("Data is empty")

@xframe_options_exempt
def detail(request,product):
    token = request.session.get('token', False)
    if not token:
        raise Http404("You do not have permission")
    global g_production
    global g_plan
    global g_year
    data = g_plan
    # print data2
    # data = production_plan_test
    # # print data
    production_plan = data[product]
    # print production_plan
    if bool(production_plan):
        line = {}
        type = ["mua_sam","san_xuat","kinh_doanh"]
        # type_plan = ["hang_ve_kh", "san_xuat_kh", "kinh_doanh_kh"]
        xArray = [0,1,2,3,4,5,6,7,8,9,10,11]
        for key in type:
            yArray = production_plan[key]['thuc_te_thang']
            line_near_reality = linear_regression(xArray,yArray)
            yArray = production_plan[key]['ke_hoach_thang']
            line_near_plan = linear_regression(xArray, yArray)
            line[key] = {
                'ke_hoach_thang':line_near_plan,
                'thuc_te_thang':line_near_reality
            }
        print base_url
        return render(request,'production_plan_detail.html',{'production':g_production,'production_plan':production_plan,'line':line,'product':product,'year':g_year,'api_url':base_url})
    return HttpResponse("Data is empty")