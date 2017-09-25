function selectProduct(){
    var e = document.getElementById("products");
    var productId = e.options[e.selectedIndex].value;
    var boms = getBoM(productId)
    $("#version").empty()
    $('#version').append($('<option>', {
            value: 'All',
            text : 'Version: All'
        }));
    $.each(boms, function (i, bom) {
        $('#version').append($('<option>', {
            value: bom.id,
            text : bom.name
        }));
    });
}

function getBoM(productId){
    var xhr = new XMLHttpRequest();
    url = "http://10.2.8.58:8090/api/v2/inv/part/export/getBomByProduct?product_id="+productId
    xhr.open("GET", url, false);
    xhr.send();

    var response = JSON.parse(xhr.responseText);
//    console.log(response['resutls'][0])
    return response['resutls']
}

function create(){
    $("#loading").show()
    $("#createReport").click(false)
    $("#products").click(false)
    $("#version").click(false)
}