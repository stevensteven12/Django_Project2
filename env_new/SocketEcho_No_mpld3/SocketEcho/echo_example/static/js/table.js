 function tableCreate(new_data) {
    var body = document.getElementById('div_Table');
    var tbl = document.getElementById('tb_id');

    tbl.setAttribute('border', '1');
/*
    var theader= document.createElement('thead');
    var tr_1 = document.createElement('tr');

    for (var i = 0; i < 9; i++) {
        var th_1 = document.createElement('th');
        switch (i) {
            case 0:
                th_1.appendChild(document.createTextNode('序號'));
                break;
            case 1:
                th_1.appendChild(document.createTextNode('商品'));
                break;
            case 2:
                th_1.appendChild(document.createTextNode('日期'));
                break;
            case 3:
                th_1.appendChild(document.createTextNode('時間'));
                break;
            case 4:
                th_1.appendChild(document.createTextNode('開盤'));
                break;
            case 5:
                th_1.appendChild(document.createTextNode('最高'));
                break;
            case 6:
                th_1.appendChild(document.createTextNode('最低'));
                break;
            case 7:
                th_1.appendChild(document.createTextNode('收盤'));
                break;
            case 8:
                th_1.appendChild(document.createTextNode('總量'));
                break;
        }
        tr_1.appendChild(th_1);
    }

    theader.appendChild(tr_1);
    tbl.appendChild(theader);
    body.appendChild(tbl)
*/
    var tbdy = document.createElement('tbody');

    var content= new_data.split('\n');
    for (var i = 1; i < content.length - 1; i++) {
        var Line = content[i];
        var array_data = Line.split(',');

        var tr = document.createElement('tr');
        for (var j = 0; j < 9; j++) {
           var td = document.createElement('td');
           if (j== 0){
               td.appendChild(document.createTextNode(array_data[13]));
           } else if (j== 7){
               td.appendChild(document.createTextNode(array_data[8]));
           } else if (j== 8){
               td.appendChild(document.createTextNode(array_data[12]));
           } else {
               td.appendChild(document.createTextNode(array_data[j]));
           }
           tr.appendChild(td);
        }
        tbdy.appendChild(tr);
    }
    tbl.appendChild(tbdy);
 //   body.appendChild(tbl);
    $(document).ready( scrollToBottom );
}

function scrollToBottom() {
   var scrollBottom = Math.max($('#tb_id').height() - $('#div_Table').height() + 20, 0);
   $('#div_Table').scrollTop(scrollBottom);
}

 function tableCreate_1() {
    var body = document.getElementById('div_Table');
    var tbl = document.createElement('table');

 //   tbl.style.width = '100%';
    tbl.setAttribute('border', '1');

    var theader= document.createElement('thead');
    var tr_1 = document.createElement('tr');

    for (var i = 0; i < 8; i++) {
        var th_1 = document.createElement('th');
        switch (i) {
            case 0:
                th_1.appendChild(document.createTextNode('商品'));
                break;
            case 1:
                th_1.appendChild(document.createTextNode('日期'));
                break;
            case 2:
                th_1.appendChild(document.createTextNode('時間'));
                break;
            case 3:
                th_1.appendChild(document.createTextNode('開盤'));
                break;
            case 4:
                th_1.appendChild(document.createTextNode('最高'));
                break;
            case 5:
                th_1.appendChild(document.createTextNode('最低'));
                break;
            case 6:
                th_1.appendChild(document.createTextNode('收盤'));
                break;
            case 7:
                th_1.appendChild(document.createTextNode('總量'));
                break;
        }
        tr_1.appendChild(th_1);
    }

    theader.appendChild(tr_1);
    tbl.appendChild(theader);
    body.appendChild(tbl)

    var tbdy = document.createElement('tbody');
    for (var i = 0; i < 30; i++) {
        var tr = document.createElement('tr');
        for (var j = 0; j < 2; j++) {
            if (i == 2 && j == 1) {
                break
            } else {
                var td = document.createElement('td');
                td.appendChild(document.createTextNode('10000'));
                i == 1 && j == 1 ? td.setAttribute('rowSpan', '2') : null;
                tr.appendChild(td);
            }
        }
        tbdy.appendChild(tr);
    }
    tbl.appendChild(tbdy);
    body.appendChild(tbl);
}