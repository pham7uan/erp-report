from django.http import HttpResponse
from django.shortcuts import render, redirect
from report.rest import *
# import report.tests
from django.views.decorators.clickjacking import xframe_options_exempt
from report.utils import *
from report.tests import *

@xframe_options_exempt
def dashboard(request):
    # production = get_reality_production()
    production = production_test
    production_plan = production_plan_test
    return render(request,'dashboard.html',{'production':production,'production_plan':production_plan})

# @xframe_options_exempt
# def area(request,product):
#     production_plan = production_plan_test
#     assign = production_plan[product]
#     print assign
#     return render(request,'area.html',{'assign':assign,'product':product})

@xframe_options_exempt
def detail(request,product):
    data = production_plan_test
    # print data
    production_plan = data[product]
    # business = production_plan[product]
    line = {}
    type = ["ke_hoach","hang_ve","san_xuat","kinh_doanh"]
    xArray = [0,1,2,3,4,5,6,7,8,9,10,11]
    for key in type:
        yArray = production_plan[key]['months']
        line_near = linear_regression(xArray,yArray)
        line[key] = line_near
    return render(request,'production_plan_detail.html',{'production_plan':production_plan,'line':line,'product':product})