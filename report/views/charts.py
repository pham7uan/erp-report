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
    # if not bool(g_plan):
    g_plan = get_reality_production_detail(year)
    g_production = get_reality_production(year)
    # print g_production
    # production = production_test
    # production_plan = production_plan_test
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
    if bool(production_plan):
        line = {}
        type = ["ke_hoach","hang_ve","san_xuat","kinh_doanh"]
        xArray = [0,1,2,3,4,5,6,7,8,9,10,11]
        for key in type:
            yArray = production_plan[key]['months']
            line_near = linear_regression(xArray,yArray)
            line[key] = line_near
        return render(request,'production_plan_detail.html',{'production':g_production,'production_plan':production_plan,'line':line,'product':product,'year':g_year})
    return HttpResponse("Data is empty")