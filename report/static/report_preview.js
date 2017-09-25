function handleModal(type,month){
    $('#modalbody').empty();
    $('#modalheader').empty();
    title =''
    table = '<div style="height:400px;overflow:auto;"><table class="table table-bordered table-striped">'
    if (type=="hang_ve"){
        title = "Kế hoạch hàng về và chi tiết hàng về tháng "+month
        thead = '<thead><tr bgcolor="#D3D3D3"><th>Sản phẩm</th>' +
                 '<th>Kế hoạch mua hàng</th><th>SL đặt</th><th>Ngày đặt</th>' +
                 '<th>SL về</th><th>Ngày về</th><tr></thread>'
        tbody = '<tbody><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody>'
        table = table + thead +tbody +'</table>'
    } else if (type=="san_xuat"){
        title = "Kế hoạch sản xuất và chi tiết sản xuất tháng "+month
        thead = '<thead><tr bgcolor="#D3D3D3"><th>Sản phẩm</th>' +
                 '<th>SL dự kiến</th><th>Ngày bắt đầu sản xuất</th><th>SL nhập kho</th>' +
                 '<th>Ngày nhập kho</th><tr></thread>'
        tbody = '<tbody><tr><td></td><td></td><td></td><td></td><td></td></tr></tbody>'
        table = table + thead +tbody +'</table>'

    } else if (type=="kinh_doanh"){
        title = "Kế hoạch kinh doanh và chi tiết giao hàng tháng "+month
        thead = '<thead><tr bgcolor="#D3D3D3"><th>Sản phẩm</th>' +
                 '<th>SL dự kiến</th><th>Ngày ký hợp đồng</th><th>SL giao hàng</th>' +
                 '<th>Ngày giao hàng</th><tr></thread>'
        tbody = '<tbody><tr><td></td><td></td><td></td><td></td><td></td></tr></tbody>'
        table = table + thead +tbody +'</table></div>'

    }

    $('#modalheader').html(title);
    $('#modalbody').append(table);

}