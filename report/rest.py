import requests
import collections
import json
base_url = 'http://10.2.8.58:8090/api/v2/'

def get_products():
    url = base_url +'inv/part/export/getListProduct'
    response = requests.get(url).json()
    return response['resutls']

def get_boms(id):
    url = base_url +'inv/part/export/getBomByProduct?product_id=' + str(id)
    response = requests.get(url)
    return response

def get_data(bom_id):
    url =base_url +'inv/part/export/TEST_REPORT?sys_bom_id=' + str(bom_id)
    response = requests.get(url).json()
    # decoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
    # print decoder.decode(response.text)
    return response

def get_reality_production(year):
    url =base_url +'inv/report_v2/GetRealityProduction?year=' + str(year)
    response = requests.get(url).json()
    return response

def get_reality_production_detail(year):
    url =base_url +'inv/report_v2/GetPlanProduction?year=' + str(year)
    response = requests.get(url).json()
    return response

