//hang ve
var receive_test = {
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
// san xuat
var produce_test = {
    'ONTv1': {
        'plan_quantity':13,
        'produce_date':'1/1/2017',
        'store_quantity':12.5,
        'store_date':'10/1/2017'
    },
    'ONTv2': {
        'plan_quantity':16,
        'produce_date':'1/1/2017',
        'store_quantity':16,
        'store_date':'10/1/2017'
    }
}
//kinh doanh
var business_test = {
    'ONTv1': {
        'plan_quantity':13,
        'contract_date':'1/1/2017',
        'delivery_quantity':12.5,
        'delivery_date':'10/1/2017'
    },
    'ONTv2': {
        'plan_quantity':16,
        'contract_date':'1/1/2017',
        'delivery_quantity':16,
        'delivery_date':'10/1/2017'
    }
}

function handleModal(type,month,key){
    $('#modalbody').empty();
    $('#modalheader').empty();
    data = receive_test
    data1 = produce_test
    data2 = business_test
    title =''
    table = '<div style="height:400px;overflow:auto;"><table class="table table-bordered table-hover">'
    if (type=="hang_ve"){
        title = "Kế hoạch hàng về và chi tiết hàng về tháng "+month
        thead = '<thead><tr bgcolor="#D3D3D3"><th>Sản phẩm</th>' +
                 '<th>Kế hoạch mua hàng</th><th>SL đặt</th><th>Ngày đặt</th>' +
                 '<th>SL về</th><th>Ngày về</th><tr></thread>'
        tbody = '<tbody>'
        for (var key in data) {
            for (i=0;i < data[key].length; i++){
                if (data[key].length > 1 && i==0){
                    tbody = tbody + '<td rowspan="' + data[key].length + '">' + key + '</td>'
                } else if (data[key].length == 1) {
                    tbody = tbody + '<tr><td>' +key+'</td>'
                }
                tbody = tbody + '<td>' +data[key][i]['plan']+'</td>'
                tbody = tbody + '<td>' +data[key][i]['order']+'</td>'
                tbody = tbody + '<td>' +data[key][i]['order_date']+'</td>'
                tbody = tbody + '<td>' +data[key][i]['receive']+'</td>'
                tbody = tbody + '<td>' +data[key][i]['receive_date']+'</td>'
                tbody = tbody + '</tr>'
            }
        }
        tbody = tbody +'</tbody>'
        table = table + thead +tbody +'</table>'
    } else if (type=="san_xuat"){
        title = "Kế hoạch sản xuất và chi tiết sản xuất tháng "+month
        thead = '<thead><tr bgcolor="#D3D3D3"><th>Sản phẩm</th>' +
                 '<th>SL dự kiến</th><th>Ngày bắt đầu sản xuất</th><th>SL nhập kho</th>' +
                 '<th>Ngày nhập kho</th><tr></thread>'
        tbody = '<tbody>'
        for (var key in data1) {
                tbody = tbody + '<tr>' + '<td>' + key +'</td>'
                for (key2 in data1[key]){
                    tbody = tbody + '<td>' + data1[key][key2] +'</td>'
                }
                tbody = tbody + '</tr>'
        }
        tbody = tbody +'</tbody>'
        table = table + thead +tbody +'</table>'

    } else if (type=="kinh_doanh"){
        title = "Kế hoạch kinh doanh và chi tiết giao hàng tháng "+month
        thead = '<thead><tr bgcolor="#D3D3D3"><th>Sản phẩm</th>' +
                 '<th>SL dự kiến</th><th>Ngày ký hợp đồng</th><th>SL giao hàng</th>' +
                 '<th>Ngày giao hàng</th><tr></thread>'
        tbody = '<tbody>'
        for (var key in data2) {
                tbody = tbody + '<tr>' + '<td>' + key +'</td>'
//                console.log(data2[key])
                for (key2 in data2[key]){

                    tbody = tbody + '<td>' + data2[key][key2] +'</td>'
                }
                tbody = tbody + '</tr>'
        }
        tbody = tbody +'</tbody>'
        table = table + thead +tbody +'</table></div>'

    }

    $('#modalheader').html(title);
    $('#modalbody').append(table);

}
//Math.floor(Math.random() * 6) + 1
function loading(){
    random =0
    random = getRandomInt(20,50)
    str = random +'%'
    $('#processing').css('width', str);
    $('#processing').html(str);
    setTimeout(function(){
        random = getRandomInt(60,90)
        str = random +'%'
        $('#processing').css('width', str);
        $('#processing').html(str);
    }, 2000);

}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}