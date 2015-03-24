function adjust_axis() {
	var xlen = document.getElementById("xInput").value;
	var ylen = document.getElementById("yInput").value;
	var x;
	var y;
	var text = '';
	for (y = 0; y <= ylen; y++) {
		if (y < 1) {
			text += '<td ></td>';
			for (x = 1; x <= xlen; x++) {
				text += '<td><b>' + x + '</b></td>';
			}
		} else {
			text += '<tr><td><b>' + y + '</b></td>';
			for (x = 1; x <= xlen; x++) {
				var imageID = x + " " + y;
				text += '<td><img class="notselected" id="' + imageID + '" src="/static/images/knit.png" ondrop="drop(event)" style="background-color:#FFFFFF" ondragover="allowDrop(event)" onclick="change_stitch';
				text += "('" + imageID + "')" + '" alt="stitch" height="24" width="24"></td>';
			}
			text += '</tr>';
		}
	}
	document.getElementById("grid").innerHTML = "";
	document.getElementById("grid").innerHTML = text;
}


function change_stitch(imageID) {
	var image = document.getElementById(imageID);
	if (image.src.match("knit")) {
		if (image.getAttribute("style") == "background-color:#000000;") {
			image.src = "/static/images/purl_white.png";
		} else {
			image.src = "/static/images/purl.png";
		}
	} else if (image.src.match("purl")) {
		if (image.getAttribute("style") == "background-color:#000000;") {
			image.src = "/static/images/drop_white.png";
		} else {
			image.src = "/static/images/drop.png";
		}
	} else {
		image.src = "/static/images/knit.png";
	}

}




function map_maker(){
	var design = "";
	var xsize = document.getElementById("xInput").value;
	var ysize = document.getElementById("yInput").value;
	for (var y = 1; y <= ysize; y++) {
		for (var x = 1; x <= xsize; x++) {
			var imageID = x + " " + y;
			var colour = document.getElementById(imageID).getAttribute("style").slice(18, 24);
			var stitch_image = document.getElementById(imageID).getAttribute("src");
			var stitch = "knit";
			switch (stitch_image) {
				case "/static/images/drop.png":
					stitch = "drop";
					break;
				case "/static/images/drop_white.png":
					stitch = "drop_white";
					break;
				case "/static/images/purl.png":
					stitch = "purl";
					break;
				case "/static/images/purl_white.png":
					stitch = "purl_white";
					break;
			}
			design += imageID + " " + stitch + " " + colour + " ";
			
			
		}
	}
	document.getElementById("design_text").value = design;
}


function select(id) {
	if (document.getElementById(id).getAttribute("class") == "selected") {
		document.getElementById(id).setAttribute("class", "notselected");
	}
	else{
		document.getElementById(id).setAttribute("class", "selected");
	}
}

function select_or_change() {
	if (document.getElementById("copymode").innerHTML == "Activate Copy Mode") {
		change_to_select();
		document.getElementById("copymode").innerHTML = "Deactivate Copy Mode";
	}
	else {
		change_to_switch();
		document.getElementById("copymode").innerHTML = "Activate Copy Mode";
	}
}

function change_to_select() {
	for (var y = 1; y <= document.getElementById("yInput").value; y++) {
		for (var x = 1; x <= document.getElementById("xInput").value; x++) {
			id = x + ' ' + y;
			document.getElementById(id).setAttribute("onclick", "select('" + id + "')");
		}
	}
}

function change_to_switch() {
	for (var y = 1; y <= document.getElementById("yInput").value; y++) {
		for (var x = 1; x <= document.getElementById("xInput").value; x++) {
			id = x + ' ' + y;
			document.getElementById(id).setAttribute("class", "notselected")
			document.getElementById(id).setAttribute("onclick", "change_stitch('" + id + "')");
		}
	}
}

function copy(){
	copylist = [];
	for (var y = 1; y <= document.getElementById("yInput").value; y++) {
		for (var x = 1; x <= document.getElementById("xInput").value; x++) {
			id = x + ' ' + y;
			if (document.getElementById(id).getAttribute("class") == "selected"){
				document.getElementById(id).setAttribute("class", "copied");
				copylist.push(String(id));
				console.log(copylist);
			}
		}
	}
}

function paste(list){
console.log(list);
	for (var y = 1; y <= document.getElementById("yInput").value; y++) {
		for (var x = 1; x <= document.getElementById("xInput").value; x++) {
			id = x + ' ' + y;
			if (document.getElementById(id).getAttribute("class") == "selected"){
				var base = id;
				break;
			}
		}
	}
	var copied_base = list[0];
	copied_base = copied_base.split(" ");
	base = base.split(" ");
	var xtrans = Number(base[0])-Number(copied_base[0]);
	var ytrans = Number(base[1])-Number(copied_base[1]);
	for (var i = 1; i<list.length; i++){
		console.log(cell);
		var cell = String(list[i]);
		var colour = document.getElementById(cell).getAttribute("style");
		var stitch = document.getElementById(cell).getAttribute("src");
		cell = cell.split(" ");
		var newx = Number(cell[0])+xtrans;
		var newy = Number(cell[1])+ytrans;
		if (newx <= document.getElementById("xInput").value && newy <= document.getElementById("yInput").value){
			var new_id = String(newx + " " + newy);
			document.getElementById(new_id).setAttribute("style", colour);
			document.getElementById(new_id).setAttribute("src", stitch);
		}
	}								
}


function allowDrop(ev) {
	ev.preventDefault();
}

function drag(ev) {
	ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
	ev.preventDefault();
	var data = ev.dataTransfer.getData("text");
	ev.target.setAttribute("style", ('background-color:' + data + ';'));
}

function convert_string(string){
    var list = string.split(" ");
	var new_list = [];
    var xmax = 1;
	var ymax = 1;
    for (var i = 0; i <= list.length-2; i++){
		if (i%4 == 0){
		    xmax = Number(list[i]);
		}
		if (i%4 == 1){
		    ymax = Number(list[i]);
		}
		if (i%4 == 2){
		    new_list.push(String(list[i]));
		}
		if (i%4 == 3){
		    new_list.push(String(list[i]));
		}
	}
	var text = "";
	var iter = 0;
	for (var y = 0; y <= ymax; y++){
	    if (y<1){
				text += '<td></td>';
				for (var x = 1; x <= xmax; x++) {
					text += '<td><b>' + x + '</b></td>';
					}
		}else{
				text += '<tr><td><b>' + y + '</b></td>';
				for (x = 1; x <= xmax; x++) {
					var stitch = new_list[iter];
				    var colour = new_list[iter+1];
					iter += 2;
					text += '<td><img  class="standard" ';
					var img_src = "";
					switch(stitch){
						case "drop":
							img_src = "/static/images/drop.png";
							break;
						case "drop_white":
							img_src = "/static/images/drop_white.png";
							break;
						case "purl":
							img_src = "/static/images/purl.png";
							break;
						case "purl_white":
							img_src = "/static/images/purl_white.png";
							break;
						case "knit":
							img_src = "/static/images/knit.png";
							break;
					    }
					text += 'src="' + img_src + '" ';
					text += 'style="background-color:#' + colour;
					text += '" alt="stitch" height="24" width="24"></td>';
					}
				text += '</tr>';
				}
		    }
			document.getElementById("pattern_grid").innerHTML = text;
	}