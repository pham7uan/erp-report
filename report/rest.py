import requests
import collections
import json
base_url = 'http://10.2.8.58:8090/api/v2/inv/part/export/'

def get_products():
    url = 'http://10.2.8.58:8090/api/v2/inv/part/export/getListProduct'
    response = requests.get(url).json()
    return response['resutls']

def get_boms(id):
    url = 'http://10.2.8.58:8090/api/v2/inv/part/export/getBomByProduct?product_id=' + str(id)
    response = requests.get(url)
    return response

def get_data(bom_id):
    url ="http://10.2.8.58:8090/api/v2/inv/part/export/TEST_REPORT?sys_bom_id=" + str(bom_id)
    response = requests.get(url).json()
    # decoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
    # print decoder.decode(response.text)
    return response

def get_reality_production():
    url =""
    response = requests.get(url).json()
    return response

