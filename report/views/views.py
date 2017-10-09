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

@csrf_exempt
def mrp_calculator(request):
    if request.method == 'POST':
        # print request.body
        json_data = json.loads(request.body.decode(encoding='UTF-8'))
        data = json_data['data']
        # data = data2.data
        mrp2.bom = data['bom']
        mrp2.materials = data['materials']
        result = mrp2.main()
        result_json = json.dumps(result)
        # print result_json
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

