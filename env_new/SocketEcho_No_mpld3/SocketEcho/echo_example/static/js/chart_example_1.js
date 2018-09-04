var x_0= 30;
var y_0= 490;
var y_end= 10;
var x_end= 690;
var interval_scale= 20;
var lowest_match_v= 100;
var lowest= 0;
var highest= 0;

var width_candle= 10;
var gap_x= 1;
var ratio= 4;
var scale_high;
var first_high, first_low;
var line_width= 1;
var draw, inner_draw;

var rect, line;
var group_all;

function draw_chart(drawing){
    var line_width= 1;
    draw = SVG(drawing).size(x_end, y_0 + 50);

 //   inner_draw= SVG(drawing).viewbox(50, 0, x_end,  y_0 + 50);
    inner_draw = SVG(drawing).size(x_end + 50, y_0 + 50);

    var set = draw.set();
    set.clear();

    var line = draw.line(x_0, y_0, x_0, y_end).stroke({ width: line_width });
    draw.line(x_0, y_0, x_end, y_0).stroke({ width: line_width });
    draw.line(x_0, y_0, x_0, y_end).stroke({ width: line_width });

    rect_dummy= draw.rect(x_end, y_0 + 50);
    rect_dummy.attr({'fill-opacity': 0, stroke: '#000', 'stroke-width': 0});
    group_all = draw.group();
 //   group_all = inner_draw.group();
    group_all.add(rect_dummy);

    // bind
    group_all.on('dragstart.namespace', function(event){

	    // event.detail.event hold the given data explained below
    })

    group_all.draggable().on('beforedrag', function(e){
      //  e.preventDefault()
        // no other events are bound
        // drag was completely prevented
    })

    group_all.draggable().on('dragmove', function(e){
      //  e.preventDefault()
        this.move(e.detail.p.x, e.detail.p.y)
        // events are still bound e.g. dragend will fire anyway
    })


//    group_all.draggable({10, 100, 200, 100, 20});
    group_all.draggable(function(x, y) {
        return { x: x < 500, y: y = y_0 + 50 }
    })

//    drag_obj();
//    aminate();
}

function aminate(){
    var input = document.querySelector('input[type=text]')
 //   var draw = SVG('drawing').viewbox(0, 0, 300, 140)
    var text = draw.text(function(add) {
	    add.tspan( input.value );
    })

    text
	    .path('M10 80 C 40 10, 65 10, 95 80 S 150 150, 180 80')
	    .animate(1000, '<>')
	    .plot('M10 80 C 40 150, 65 150, 95 80 S 150 10, 180 80')
	    .loop(true, true);

    input.addEventListener('keyup', updateText(text));

    function updateText(textPath) {
	    return function() {
		    textPath.tspan(this.value);
	    }
    }
}

function data_input(input_array){

    var parsedTest = JSON.parse(input_array);
    var array_size= parsedTest.length;
    var data_array= new Array(array_size);

    var single_array = parsedTest[0];
    first_high= single_array[2];
    first_low= single_array[3];
    lowest= first_low;
    ratio= 1;

    get_high_low(parsedTest);

    for (i=0; i< 8; i++){
        var scale_y2 = draw.text(String(lowest + interval_scale * i)); // first_low, 10757  is located at 0, first_low is 100 over 0
        scale_y2.move(0, (y_0 - lowest_match_v) - interval_scale * i*ratio).font({ fill: '#000000', size: 10 }); // point 100: first low
    }

 //   for (i in parsedTest) {
    var start_no= 0;
    if(array_size > 60){ start_no= array_size - 60;}

    for (i= 0; i< array_size; i++) {
       single_array = parsedTest[i];
       raw_candle(single_array, i, start_no);
    }

    group_all.draggable();
}

function get_high_low(parsedTest){
    for (i in parsedTest) {
       single_array = parsedTest[i];
       var high_v= single_array[2];
       var low_v= single_array[3];
       if (high_v > highest)
         highest= high_v;
       if (low_v < lowest)
         lowest= low_v;
    }

    scale_high= y_0 - y_end;
    var range_v= highest - lowest;
    ratio= (scale_high - lowest_match_v * 2) / range_v;
}

function raw_candle(input_array, index, start_no){
    var date_time= input_array[0];
    var open_v= input_array[1];
    var high_v= input_array[2];
    var low_v= input_array[3];
    var close_v= input_array[4];
    var volume_v= input_array[5];
    var color_code;
    var height_candle_original= close_v - open_v;
    var height_stick_original= high_v - low_v;

    if (height_candle_original >= 0){
        color_code= '#FF0000';
    } else {
        color_code= '#228B22';
        height_candle_original= height_candle_original * (-1);
     //   open_v= close_v;
    }

    // first_low: Y_0-100---> lowest: Y_0-100
    var height_candle= height_candle_original * ratio;
    var height_stick= height_stick_original * ratio;

    var y_open= (y_0-100) - (open_v - lowest) * ratio;
    var line_low_R= (y_0-100) - (low_v - lowest) * ratio;
    var line_high_R= (y_0-100) - (high_v - lowest) * ratio;

    line= draw.line(x_0 + (width_candle + gap_x) * (index - start_no) + (width_candle + gap_x)/2, line_low_R,
        x_0 + (width_candle + gap_x) * (index - start_no) + (width_candle + gap_x)/2, line_high_R).stroke({ width: line_width });
    line.stroke({ color: color_code});

    rect= draw.rect(width_candle, height_candle).move(x_0 + (width_candle + gap_x) * (index - start_no), y_open).fill(color_code);

    var scale_x0 = draw.text(date_time);
    scale_x0.move(10 + x_0 + (width_candle + gap_x) * ((index - start_no) - 2) + (width_candle + gap_x)/2 + 2, y_0 + 25).font({ fill: '#000000', family: 'Inconsolata', size: 10 });
    scale_x0.transform({ rotation: 0 }).transform({ rotation: 90 })

    group_all.add(line);
    group_all.add(rect);
    group_all.add(scale_x0);

    rect.click(function() {
        this.fill({ color: '#228B22' });
    });

    var line_x, line_y;
    rect.mouseover(function() {
        var attr_client = this.attr();
        line_x = draw.line(x_0, attr_client['y'], x_end, attr_client['y']).stroke({ width: line_width });
        line_y = draw.line(attr_client['x'] + (width_candle + gap_x)/2, y_0,
                 attr_client['x'] + (width_candle + gap_x)/2, y_end).stroke({ width: line_width });
    //    this.fill({ color: '#FF0000' });

    });

    rect.mouseout(function() {
        line_x.move(-1, -1);
        line_y.move(-1, -1);
    });

    var line_upperY, line_downY;
    line.mouseover(function() {
        var attr_client = this.attr();
        line_upperY = draw.line(x_0, attr_client['y1'], x_end, attr_client['y1']).stroke({ width: line_width });
        line_downY = draw.line(x_0, attr_client['y2'], x_end, attr_client['y2']).stroke({ width: line_width });
        this.fill({ color: '#FF0000' });


    });

    line.mouseout(function() {
        line_upperY.move(-1, -1);
        line_downY.move(-1, -1);
    });

}

function drag_obj(){
    var rect_1 = draw.rect(100, 100);
    rect_1.draggable();
/*
    // set scope
    draw.viewbox(0, 0, 1000, 2100);
    // get zoom ratio
    var box = draw.viewbox();
    var zoom = box.zoom;
*/
/*
    // draw transformed rect
    var rect_2 = draw.rect(175,175).move(75,75).rotate(20).scale(1, 0.5);
    // draw bbox
    var b = rect_2.bbox();
    draw.rect(b.width, b.height).addClass('box').move(b.x, b.y);
    */

    var rect_2 = draw.rect(175,175).move(75,75).rotate(20).scale(1, 0.5);

    var group = draw.group();
    group.add(rect_1);
    group.add(rect_2);
    group.draggable();

}