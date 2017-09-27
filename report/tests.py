# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict
from django.test import TestCase
import data2
# Create your tests here.
production_test = [
    {
        "name": "ONT",
        "sum": 91654,
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
        "sum": 0,
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
        "sum": 79940,
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
        "sum": 0,
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
        "sum": 0,
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
        "ke_hoach": {
            "sum": 19352000,
            "months": [
                0,
                0,
                1710000,
                2642000,
                4500000,
                0,
                8100000,
                2400000,
                0,
                0,
                0,
                0
            ]
        },
        "hang_ve": {
            "sum": 907902.2537899185,
            "months": [
                0,
                0,
                1710000,
                2642000,
                4500000,
                0,
                8100000,
                2400000,
                0,
                0,
                0,
                0
            ]
        },
        "san_xuat": {
            "sum": 91654,
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
        "kinh_doanh": {
            "sum": 1000,
            "months": [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1000,
                0,
                0,
                0,
                0
            ]
        }
    },
    "SmartBox&STB": {
        "ke_hoach": {
            "sum": 540000,
            "months": [
                0,
                0,
                0,
                0,
                540000,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ]
        },
        "hang_ve": {
            "sum": 365530,
            "months": [
                0,
                0,
                0,
                0,
                540000,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ]
        },
        "san_xuat": {
            "sum": 0,
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
        "kinh_doanh": {
            "sum": 0,
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
    },
    "DVB-T2": {
        "ke_hoach": {
            "sum": 3260000,
            "months": [
                0,
                0,
                0,
                0,
                1180000,
                0,
                2000000,
                80000,
                0,
                0,
                0,
                0
            ]
        },
        "hang_ve": {
            "sum": 331268,
            "months": [
                0,
                0,
                0,
                0,
                1180000,
                0,
                2000000,
                80000,
                0,
                0,
                0,
                0
            ]
        },
        "san_xuat": {
            "sum": 79940,
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
        "kinh_doanh": {
            "sum": 0,
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
    },
    "SmartPhone": {
        "ke_hoach": {
            "sum": 0,
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
        "hang_ve": {
            "sum": 0,
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
        "san_xuat": {
            "sum": 0,
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
        "kinh_doanh": {
            "sum": 0,
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
    },
    "Sản phẩm khác": {
        "ke_hoach": {
            "sum": 3900200,
            "months": [
                0,
                0,
                0,
                0,
                0,
                0,
                3300000,
                0,
                600200,
                0,
                0,
                0
            ]
        },
        "hang_ve": {
            "sum": 3314238,
            "months": [
                0,
                0,
                0,
                0,
                0,
                0,
                3300000,
                0,
                600200,
                0,
                0,
                0
            ]
        },
        "san_xuat": {
            "sum": 0,
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
        "kinh_doanh": {
            "sum": 0,
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
    }
}

hang_ve_test = {
	'ONTv1':[{
		'plan':15,
		'order':13,
		'order_date':'1/1/2017',
		'receive':12.5,
		'receive_date':'2/1/2017'
	},{
		'plan':15,
		'order':13,
		'order_date':'1/1/2017',
		'receive':0.5,
		'receive_date':'3/1/2017'
	}],
	'ONTv2':[{
		'plan':15,
		'order':15,
		'order_date':'1/1/2017',
		'receive':12.5,
		'receive_date':'2/1/2017'
	}]
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