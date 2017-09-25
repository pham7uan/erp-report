
window.onload = function() {
    render_treeview()
};

function btnTree() {
    console.log('btnTree')
    render(false)
};

function btnTable() {
    console.log('btnTable')
    render(true)
};

function render(view){
       if (view == false){
        $('#treeviewtag').show();
        $('#tableviewtag').hide();
       } else {
        $('#treeviewtag').hide();
        $('#tableviewtag').show();
       }
}

function render_treeview(){
//      console.log(result);
      $('#treeviewtag').hide();
      Object.keys(result).forEach(function(key) {
        value = result[key];
        label = '<div class="row">'
        label = label + '<h2>'+key+'</h2>'
        label = label + '<label>Số sản phẩm có thể sản xuất:'+value.max+'</label>'
        label = label + '<p>Chi tiết: </p>'
        label = label +'</div>'
        $('#treeviewtag').append(label);
        treeview = '<table class="tree" id="treeview"></table>'
        $('#treeviewtag').append(treeview);
        materials_list = value.materials_list
        Object.keys(materials_list).forEach(function(k) {
            material = materials_list[k]
//            console.log(material)
            level = material[0].split('_')[1]
            name = material[0].split('_')[0]
            subLevel = level.split('.')
//            id = level.replace('.','')
            var id = level
            id = id.replace(/\./g,'')
            if (subLevel.length == 1){
               tr = '<tr class="treegrid-' +id +'"' + 'id="node_'+id +'"' +'>'
                td = '<td>' + level +'&nbsp</td>'
                td = td + '<td>&nbsp' + name +'&nbsp</td>'
                td = td + '<td>&nbsp' + material[1] +'</td>'
                tr = tr + td + '</tr>'
//                console.log(tr)
                $('#treeview').append(tr);
            }
            if (subLevel.length > 1){
                parent =subLevel[0]
                for (i =1; i <subLevel.length; i++){

                    if (i == subLevel.length -1){
                        tr = '<tr class="treegrid-' +id +' ' +'treegrid-parent-'+parent +'"' + 'id="node_'+id +'"' +'>'
                        td = '<td>' + level +'&nbsp</td>'
                        td = td + '<td>&nbsp' + name +'&nbsp</td>'
                        td = td + '<td>&nbsp' + material[1] +'&nbsp</td>'
                        tr = tr + td + '</tr>'
//                        console.log(tr)
                        $('#treeview').append(tr);
                    }
                    parent = parent + subLevel[i]
                }
            }


        });
    });
}

//<table class="tree">
//	<tr class="treegrid-1">
//		<td>Root node</td><td>Additional info</td>
//	</tr>
//	<tr class="treegrid-2 treegrid-parent-1">
//		<td>Node 1-1</td><td>Additional info</td>
//	</tr>
//	<tr class="treegrid-3 treegrid-parent-1">
//		<td>Node 1-2</td><td>Additional info</td>
//	</tr>
//	<tr class="treegrid-4 treegrid-parent-3">
//		<td>Node 1-2-1</td><td>Additional info</td>
//	</tr>
//</table>
