from django.http import HttpResponse
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
    global g_production
    global g_plan
    global g_year
    g_year = year
    # g_plan = get_reality_production_detail(year)
    # g_production = get_reality_production(year)

    g_production = production_test
    g_plan = production_plan_test
    if bool(g_production):
        return render(request,'dashboard.html',{'production':g_production,'production_plan':g_plan,'year':year})
    return HttpResponse("Data is empty")

@xframe_options_exempt
def detail(request,product):
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

        # reality_dict={}
        # plan_dict={}
        # pass_plan_dict={}
        # virtual_plan={}
        # for k in range(1,4):
        #     reality = production_plan[type[k]]['months']
        #     plan = production_plan[type_plan[k]]['months']
        #     tmp_plan =[]
        #     tmp_relity=[]
        #     tmp_pass_plan=[]
        #     tmp_virtual_plan=[]
        #     for i in range(0,12):
        #         if plan[i] >= reality[i]:
        #             tmp_plan.append(plan[i] - reality[i])
        #             tmp_relity.append(reality[i])
        #             tmp_pass_plan.append(0)
        #             tmp_virtual_plan.append(0)
        #         else:
        #             tmp_plan.append(0)
        #             tmp_relity.append(0)
        #             tmp_pass_plan.append(reality[i] - plan[i])
        #             tmp_virtual_plan.append(plan[i])
        #     reality_dict[type[k]] = tmp_relity
        #     plan_dict[type_plan[k]] = tmp_plan
        #     pass_plan_dict[type[k]] = tmp_pass_plan
        #     virtual_plan[type_plan[k]] = tmp_virtual_plan
        #
        # plan_dict['ke_hoach'] = production_plan['ke_hoach']['months']
        # reality_dict['ke_hoach'] = production_plan['ke_hoach']['months']
        #     # print reality_dict
        #     # print plan_dict
        #
        # return render(request,'production_plan_detail.html',{'production':g_production,'production_plan':production_plan,
        #                                                      'line':line,'product':product,'year':g_year,
        #                                                      'reality_dict':reality_dict,'plan_dict':plan_dict,
        #                                                      'pass_plan_dict':pass_plan_dict,'virtual_plan':virtual_plan})
        return render(request,'production_plan_detail.html',{'production':g_production,'production_plan':production_plan,'line':line,'product':product,'year':g_year})
    return HttpResponse("Data is empty")