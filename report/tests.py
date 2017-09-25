# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict
from django.test import TestCase
import data2
# Create your tests here.
production_test = [
			{
				"name": 'ONT',
				"sum" : 2007494,
				"months": 9
			},
            {
                "name": 'SP khac',
                "sum": 6,
                "months": 9
            },
			{
				"name": 'SMB & STB',
				"sum" : 297987,
				"months": 9
			},
            {
                "name": 'DVB',
                "sum": 52926,
                "months": 9
            },
            {
                "name": 'Smartphone',
                "sum": 22474,
                "months": 9
            },


		]

production_plan_test = {
	"ONT" : {
				"ke_hoach" : {
				    "sum": 2033000,
				    "months": [233000,200000,160000,160000,160000,160000,160000,160000,160000,160000,160000,160000],
				    "ton_kho": 0,
				    "so_luong_bo_sung": 0
			    },
				"hang_ve" : {
					"sum": 1793000,
					"months": [201000,153000,187000,152000,230000,220000,300000,350000,0,0,0,0],
					"ton_kho": 0,
					"so_luong_bo_sung": 489717
				},
				"san_xuat" : {
					"sum": 2007494,
					"months": [169224,170489,199878,136403,146500,180000,180000,135000,135000,135000,175000,245000],
					"ton_kho": 0,
					"so_luong_bo_sung": 0
				},
				"kinh_doanh" : {
					"sum": 1303283,
					"months": [166547,163840,170753,129889,150700,	145804,	112950,	111150,	111150,	0,	26500,	1400],
					"ton_kho": 0,
					"so_luong_bo_sung": 0
				},
				"luy_ke_ton_ke_hoach": 0,
				"luy_ke_ton_hang_ve": 0,
				"luy_ke_ton_kinh_doanh": 0
			},
	"SMB & STB" : {
				"ke_hoach" : {
				    "sum": 1007000,
				    "months": [105000,	82000,	82000,	82000,	82000,	82000,	82000,	82000,	82000,	82000,	82000,	82000],
				    "ton_kho": 0,
				    "so_luong_bo_sung": 0
			    },
				"hang_ve" : {
					"sum": 231848,
					"months": [44000,45320,680,30000,31848,70000,10000,	0,0,0,0,0],
					"ton_kho": 0,
					"so_luong_bo_sung": 66152
				},
				"san_xuat" : {
					"sum": 298399,
					"months": [28772,48751,16827,15662,12975,81000,29000,0,65000,0,0,0],
					"ton_kho": 412,
					"so_luong_bo_sung": 0
				},
				"kinh_doanh" : {
					"sum": 298,
					"months": [2000,11770,13000,10800,19460,24424,24424,35424,35424,35424,40424,45426],
					"ton_kho": 0,
					"so_luong_bo_sung": 0
				},
				"luy_ke_ton_ke_hoach": 0,
				"luy_ke_ton_hang_ve": 0,
				"luy_ke_ton_kinh_doanh": 0
			},
	"DVB": {
				"ke_hoach" : {
				    "sum": 1010000,
				    "months": [20000,90000,90000,90000,90000,90000,90000,90000,90000,90000,90000,90000],
				    "ton_kho": 0,
				    "so_luong_bo_sung": 0
			    },
				"hang_ve" : {
					"sum": 300,
					"months": [0,0,0,0,100000,200000,0,0,0,0,0,0],
					"ton_kho": 0,
					"so_luong_bo_sung": 225308
				},
				"san_xuat" : {
					"sum": 603952,
					"months": [18920,880,0,0,82860,30600,126000,120000,	0,110000,40000,0],
					"ton_kho": 74692,
					"so_luong_bo_sung": 0
				},
				"kinh_doanh" : {
					"sum": 600,
					"months": [0,0,0,0,0,173722,100000,100000,76278,50000,50000,50000],
					"ton_kho": 0,
					"so_luong_bo_sung": 0
				},
				"luy_ke_ton_ke_hoach": 0,
				"luy_ke_ton_hang_ve": 0,
				"luy_ke_ton_kinh_doanh": 0
			},
	"Smartphone": {
				"ke_hoach" : {
				    "sum": 612000,
				    "months": [12000,20000,40000,60000,60000,60000,60000,60000,60000,60000,60000,60000],
				    "ton_kho": 0,
				    "so_luong_bo_sung": 0
			    },
				"hang_ve" : {
					"sum": 12,
					"months": [0,12,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
					"ton_kho": 0,
					"so_luong_bo_sung": 18676
				},
				"san_xuat" : {
					"sum": 31964,
					"months": [1754,529,390,120,7681,2000,2000,2000,6000,	0,	0,	0],
					"ton_kho": 9490,
					"so_luong_bo_sung": 0
				},
				"kinh_doanh" : {
					"sum": 30676,
					"months": [2669,2669,2669,2669,5000,5000,2000,2000,2000,2000,2000,0],
					"ton_kho": 0,
					"so_luong_bo_sung": 0
				},
				"luy_ke_ton_ke_hoach": 0,
				"luy_ke_ton_hang_ve": 0,
				"luy_ke_ton_kinh_doanh": 0
			},
	"Sp khac":{
				"ke_hoach" : {
				    "sum": 0,
				    "months": [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
				    "ton_kho": 0,
				    "so_luong_bo_sung": 0
			    },
				"hang_ve" : {
					"sum": 0,
					"months": [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
					"ton_kho": 0,
					"so_luong_bo_sung": 6
				},
				"san_xuat" : {
					"sum": 6,
					"months":  [0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	4,	1],
					"ton_kho": 0,
					"so_luong_bo_sung": 0
				},
				"kinh_doanh" : {
					"sum": 6,
					"months": [0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	4,	1],
					"ton_kho": 0,
					"so_luong_bo_sung": 0
				},
				"luy_ke_ton_ke_hoach": 0,
				"luy_ke_ton_hang_ve": 0,
				"luy_ke_ton_kinh_doanh": 0
			},
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