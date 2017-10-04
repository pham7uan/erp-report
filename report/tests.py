# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict
from django.test import TestCase
import data2
# Create your tests here.
production_test = [
    {
        "name": "ONT",
        "sum": 19352000,
        "months": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            91654,
            0,
            0,
            0,
            0
        ]
    },
    {
        "name": "SmartBox&STB",
        "sum": 14352000,
        "months": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ]
    },
    {
        "name": "DVB-T2",
        "sum": 11352000,
        "months": [
            0,
            0,
            0,
            0,
            0,
            0,
            1320,
            54460,
            24160,
            0,
            0,
            0
        ]
    },
    {
        "name": "SmartPhone",
        "sum": 9352000,
        "months": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ]
    },
    {
        "name": "Sản phẩm khác",
        "sum": 19352,
        "months": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0
        ]
    }
]

production_plan_test = {
    "ONT": {
        "mua_sam": {
            "ke_hoach": 19352000,
            "thuc_te":17352000,
            "ke_hoach_thang":[0,0,1710000,2642000,4500000,5750000,5790000,7010000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,2042000,4100000,1050000,1090000,2010000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
        "san_xuat": {
            "ke_hoach": 16352000,
            "thuc_te":17352000,
            "ke_hoach_thang":[0,0,1710000,2642000,4500000,1750000,1790000,2010000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,2042000,4100000,1050000,1090000,2010000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
        "kinh_doanh": {
            "ke_hoach": 11352000,
            "thuc_te":10352000,
            "ke_hoach_thang":[0,0,1710000,2642000,4500000,0,8100000,2400000,0,0,0,0],
            "thuc_te_thang":[0,0,1710000,2642000,4500000,0,8100000,2400000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
    },
    "SmartBox&STB": {
        "mua_sam": {
            "ke_hoach": 10352000,
            "thuc_te":9352000,
            "ke_hoach_thang":[0,0,1210000,264000,950000,0,1100000,840000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,264000,450000,0,900000,640000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
        "san_xuat": {
            "ke_hoach": 9352000,
            "thuc_te":7352000,
            "ke_hoach_thang":[0,0,1010000,214000,550000,0,1100000,840000,0,0,0,0],
            "thuc_te_thang":[0,0,1000000,204000,750000,0,900000,640000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
        "kinh_doanh": {
            "ke_hoach": 9002000,
            "thuc_te":7352000,
            "ke_hoach_thang":[0,0,1210000,264000,950000,0,1100000,840000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,264000,450000,0,900000,640000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
    },
    "DVB-T2": {
        "mua_sam": {
            "ke_hoach": 5352000,
            "thuc_te":6352000,
            "ke_hoach_thang":[0,0,1210000,264000,950000,0,1100000,840000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,264000,450000,0,900000,640000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
        "san_xuat": {
            "ke_hoach": 1352000,
            "thuc_te":1052000,
            "ke_hoach_thang":[0,0,1210000,264000,950000,0,1100000,840000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,264000,450000,0,900000,640000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
        "kinh_doanh": {
            "ke_hoach": 1052000,
            "thuc_te":1052000,
            "ke_hoach_thang":[0,0,1210000,264000,950000,0,1100000,840000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,264000,450000,0,900000,640000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
    },
    "SmartPhone": {
        "mua_sam": {
            "ke_hoach": 8352000,
            "thuc_te":8052000,
            "ke_hoach_thang":[0,0,1210000,264000,950000,0,1100000,840000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,264000,450000,0,900000,640000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
        "san_xuat": {
            "ke_hoach": 8352000,
            "thuc_te":7352000,
            "ke_hoach_thang":[0,0,1210000,264000,950000,0,1100000,840000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,264000,450000,0,900000,640000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
        "kinh_doanh": {
            "ke_hoach": 8352000,
            "thuc_te":2352000,
            "ke_hoach_thang":[0,0,1210000,264000,950000,150000,1100000,840000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,264000,450000,90000,900000,640000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
    },
    "Sản phẩm khác": {
        "mua_sam": {
            "ke_hoach": 352000,
            "thuc_te":152000,
            "ke_hoach_thang":[0,0,1210000,264000,950000,250000,1100000,840000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,264000,450000,200000,900000,640000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
        "san_xuat": {
            "ke_hoach": 352000,
            "thuc_te":102000,
            "ke_hoach_thang":[0,0,1210000,264000,950000,0,1100000,840000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,264000,450000,0,900000,640000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
        "kinh_doanh": {
            "ke_hoach": 352000,
            "thuc_te":10200,
            "ke_hoach_thang":[0,0,1210000,264000,950000,0,1100000,840000,0,0,0,0],
            "thuc_te_thang":[0,0,1010000,264000,450000,0,900000,640000,0,0,0,0],
            "ton_kho":125232,
            "so_luong_bo_xung":0,
        },
    }
}

def check_minimum():
    data = data2.data
    bom = data['bom']
    materials = data['materials']
    check_result ={}
    for key, value in bom.iteritems():
        # print key
        sum =0
        min = value[1]
        for v in value[0]:
           sum = sum + int(materials[v])

        if sum < min:
            check_result[key] = value[0]
    # print check_result
    # result_json = json.dumps(check_result)

# check_minimum()

# import socket
# print socket.gethostbyname(socket.gethostname())