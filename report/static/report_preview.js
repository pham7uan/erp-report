//HOST = 'http://10.2.8.28:8090/api/v2/inv/report_v2/'
function handleModal(type,month){
    $('#modalbody').empty();
    $('#modalheader').empty();
    param = 'type='+type+'&'+'year='+year+'&'+'month='+month+'&'+'product='+product
    var url = api_url + 'inv/report_v2/GetDetailPlanProduction?' + param
    console.log(url)
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.send();

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            renderTable(type,month,xhr.responseText)
        }
    }
}


function renderTable(type,month,response){
    var tmp = JSON.parse(response)
    var data = tmp['results']
//    console.log(data)



    title =''
    table = '<div class="table-scrollable"><table class="table table-striped table-bordered table-hover">'
    if (type=="mua_sam"){
        title = "Kế hoạch mua sắm và chi tiết mua sắm tháng "+month
        thead = '<thead><tr bgcolor="#D3D3D3"><th>Sản phẩm</th>' +
                 '<th>Kế hoạch mua hàng</th><th>SL đặt</th><th>Ngày đặt</th>' +
                 '<th>SL về</th><th>Ngày về</th><tr></thread>'
        tbody = '<tbody>'
        var pr =''
        var order_date =''
        var plan =''
        var order=''
        for (var key in data) {
            for (i=0;i < data[key].length; i++){
                if (pr == key){
                    tbody = tbody + '<td></td>'
                } else {
                    tbody = tbody + '<tr><td>' +key+'</td>'
                }
                if (order_date == data[key][i]['order_date'] && order == data[key][i]['order'] && plan == data[key][i]['plan']) {
                    tbody = tbody + '<td></td>'
                    tbody = tbody + '<td></td>'
                    tbody = tbody + '<td></td>'

                } else {
                    tbody = tbody + '<td>' +data[key][i]['plan']+'</td>'
                    tbody = tbody + '<td>' +data[key][i]['order']+'</td>'
                    tbody = tbody + '<td>' +data[key][i]['order_date']+'</td>'

                }

                tbody = tbody + '<td>' +data[key][i]['receive']+'</td>'
                tbody = tbody + '<td>' +data[key][i]['receive_date']+'</td>'
                tbody = tbody + '</tr>'

                pr = key
                order_date = data[key][i]['order_date']
                order = data[key][i]['order']
                plan = data[key][i]['plan']
            }
        }
        tbody = tbody +'</tbody>'
        table = table + thead +tbody +'</table>'

    }
    else if (type=="san_xuat"){
//        console.log(data)
        title = "Kế hoạch sản xuất và chi tiết sản xuất tháng "+month
        thead = '<thead><tr bgcolor="#D3D3D3"><th>Sản phẩm</th>' +
                 '<th>SL dự kiến</th><th>Ngày bắt đầu sản xuất</th><th>SL nhập kho</th>' +
                 '<th>Ngày nhập kho</th><tr></thread>'
        tbody = '<tbody>'
        for (var key in data) {
                count = data[key]['nhap_kho'].length
                tbody = tbody + '<tr>' + '<td>' + key +'</td>'
                tbody = tbody + '<td>' +data[key]['du_kien']+'</td>'
                tbody = tbody + '<td>' +data[key]['ngay_bat_dau']+'</td>'

                if (count > 0){
                    tbody = tbody + '<td>' +data[key]['nhap_kho'][0]['so_luong']+'</td>'
                    tbody = tbody + '<td>' +data[key]['nhap_kho'][0]['ngay_nhap']+'</td>'
                    tbody = tbody + '</tr>'


                    if (count > 1){
                        for (var i=1; i< count;i++){
                            tbody = tbody + '<td></td>'
                            tbody = tbody + '<td></td>'
                            tbody = tbody + '<td></td>'
                            tbody = tbody + '<td>' +data[key]['nhap_kho'][i]['so_luong']+'</td>'
                            tbody = tbody + '<td>' +data[key]['nhap_kho'][i]['ngay_nhap']+'</td>'
                            tbody = tbody + '</tr>'
                    }
                    }
                } else {
                    tbody = tbody + '<td></td>'
                    tbody = tbody + '<td></td>'
                    tbody = tbody + '</tr>'
                }


        }
        tbody = tbody +'</tbody>'
        table = table + thead +tbody +'</table>'

    }
    else if (type=="kinh_doanh"){
        title = "Kế hoạch kinh doanh và chi tiết giao hàng tháng "+month
        thead = '<thead><tr bgcolor="#D3D3D3"><th>Sản phẩm</th><th>Số hợp đồng</th>' +
                 '<th>SL dự kiến</th><th>Ngày ký hợp đồng</th><th>SL giao hàng</th>' +
                 '<th>Ngày giao hàng</th><th>Tình trạng</th><tr></thread>'
        tbody = '<tbody><tr>'
        if (data.length >0){
            data = data[0]
            tbody = tbody + '<td>' +product+'</td>'
            tbody = tbody + '<td>' +data['so_hop_dong']+'</td>'
            tbody = tbody + '<td>' +data['so_luong_hop_dong']+'</td>'
            tbody = tbody + '<td>' +data['ngay_ki']+'</td>'
            tbody = tbody + '<td>' +data['so_luong_giao_hang']+'</td>'
            tbody = tbody + '<td>' +data['ngay_giao']+'</td>'
            tbody = tbody + '<td>' +data['tinh_trang']+'</td>'
        }
        tbody = tbody +'</tr></tbody>'
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