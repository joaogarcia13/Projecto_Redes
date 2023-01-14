function clearAllTimers() {
    // Clear Intervals
    // Get a reference to the last interval + 1
    const interval_id = window.setInterval(function(){}, Number.MAX_SAFE_INTEGER);

    // Clear any timeout/interval up to that id
    for (let i = 1; i < interval_id; i++) {
      window.clearInterval(i);
    }

    // Clear Timeouts
    var id = window.setTimeout(function() {}, 0);
    while (id--) {
        window.clearTimeout(id); // will do nothing if no timeout with id is present
    }
}

async function getInfo() {
    // JQuery
    $('.device-card').each(function(device) {
        let deviceID = $(this).attr('device');

        try {
            const request = new Request('http://127.0.0.1:8000/devices/external/getinfo/'+deviceID);

            fetch(request)
                .then((response) => {
                    if (response.status === 200) {
                      return response.json();
                    } else {
                      throw new Error('Something went wrong on API server!');
                      return null;
                    }
                })
                .then((response) => {
                    let json_parse = JSON.parse(response.data);
                    console.log(json_parse);
                    let temp = parseFloat(json_parse.temp.value).toFixed(2);
                    let cpu = parseFloat(json_parse.cpu.value).toFixed(1);
                    let memory = parseFloat(json_parse.memory.value).toFixed(2);

                    $(this).find("#device_temp").text(temp);
                    $(this).find("#device_cpu").text(cpu);
                    $(this).find("#device_mem").text(memory);
                    $(this).find(".status-word").html('<span>Ativo</span> <icon class="tim-icons icon-check-2"></icon>').css("color", "green");
                }).catch((error) => {
                    console.log('error',error);
                    $(this).find(".status-word").html('<span>Inativo</span> <icon class="tim-icons icon-simple-remove"></icon>').css("color", "red");
                    return null;
                });
        } catch (error) {
            console.error(error);
        }
    });
}

function switch_toggle_api(id, command) {
    console.log('id',id,'command',command);
    $.ajax({
        url: 'http://127.0.0.1:8000/devices/external/toggle_switch/'+id,
        type: 'GET',
        data: {'data': command},
        success: function(data) {
            showNotification('top','center','tim-icons icon-check-2','success','Switch '+command+' successful');
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            showNotification('top','center','tim-icons icon-sound-wave','danger','Failed: '+errorThrown);
        }
    });
}

function create_wifi_api(id) {
    var obj = {
        'wifi_ssid': document.getElementById("wifi_name").value,
        'wifi_pwd': document.getElementById("wifi_password").value
    }
    var $crf_token = $('#create_wifi_device [name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url: 'http://127.0.0.1:8000/devices/external/create_wifi/'+id,
        type: 'POST',
        data: obj,
        headers: {"X-CSRFToken": $crf_token},
        success: function(data){
            console.log(data);
            showNotification('top','center','tim-icons icon-check-2','success','Created successful');
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            showNotification('top','center','tim-icons icon-sound-wave','danger','Failed: '+errorThrown);
        }
    });
}

function kill_network_api(id) {
    //var $crf_token = $('#create_wifi_device [name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url: 'http://127.0.0.1:8000/devices/external/killnetwork/'+id,
        type: 'GET',
        success: function(data){
            console.log(data);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            showNotification('top','center','tim-icons icon-sound-wave','danger','Failed: '+errorThrown);
        }
    });
}

function edit_api(id) {
    var obj = {
        'device_id': document.getElementById("device_id").value,
        'name': document.getElementById("device_name").value,
        'ip': document.getElementById("device_ip").value,
        'mac_address': document.getElementById("device_mac_address").value,
        'wifi_ssid': document.getElementById("device_ssid").value,
        'wifi_pwd': document.getElementById("device_pwd").value,
        'type': document.getElementById("device_type").value,
        'status': document.getElementById("device_status").checked
    };
    console.log(obj);

    var $crf_token = $('#edit_device [name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url: 'http://127.0.0.1:8000/api/devices/'+id+'/update',
        type: 'PUT',
        data: obj,
        headers: {"X-CSRFToken": $crf_token},
        success: function(result) {
            console.log(result);
            showNotification('top','center','tim-icons icon-check-2','success','Edited successful');
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log("Status: " + textStatus + "\nError: " + errorThrown);
            showNotification('top','center','tim-icons icon-sound-wave','danger','Failed: '+errorThrown);
        }
    });
}

function getDataGraph(){
    $.ajax({
        url: 'http://127.0.0.1:8000/api/graph',
        type: 'GET',
        success: function(result) {
            console.log(result);
        }
    });
}

function showNotification(from, align, icon, type, message) {
    // type = ['primary', 'info', 'success', 'warning', 'danger'];

    if (icon == null || icon == '') icon="tim-icons icon-bell-55";
    if (type == null || type == '') type='primary';

    $.notify({
      icon: icon,
      message: message, //"Welcome to <b>Black Dashboard</b> - a beautiful freebie for every web developer."
    }, {
      type: type,
      timer: 1000,
      delay: 1000,
      placement: {
        from: from,
        align: align
      }
    });
}

function createChart(element, data) {
    gradientChartOptionsConfigurationWithTooltipPurple = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(225,78,202,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }]
      }
    };

    ctx = element.getContext("2d");

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(72,72,176,0.2)');
    gradientStroke.addColorStop(0.2, 'rgba(72,72,176,0.0)');
    gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors

    var chartData = {
      labels: ['JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
      datasets: [{
        label: "Data",
        fill: true,
        backgroundColor: gradientStroke,
        borderColor: '#d048b6',
        borderWidth: 2,
        borderDash: [],
        borderDashOffset: 0.0,
        pointBackgroundColor: '#d048b6',
        pointBorderColor: 'rgba(255,255,255,0)',
        pointHoverBackgroundColor: '#d048b6',
        pointBorderWidth: 20,
        pointHoverRadius: 4,
        pointHoverBorderWidth: 15,
        pointRadius: 4,
        data: data,
      }]
    };

    var myChart = new Chart(ctx, {
      type: 'line',
      responsive: true,
      data: chartData,
      options: gradientChartOptionsConfigurationWithTooltipPurple
    });
}

function get_map_api() {
	$.ajax({
		type: "GET",
		url: "http://127.0.0.1:8000/api/devices/polygons",
	}).then(function(data) {
	    console.log('map api',data);
		getBlueprint(data);
	});
}

function setMap() {
    var map = L.map('map').setView([40.57432,-8.44378], 20); // ESTGA

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([40.57376,-8.44412]).addTo(map); // monobloco TI
    L.marker([40.57438,-8.44344]).addTo(map) // sala 10
        .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
        //.openPopup();
}

// Area/Zones options
var areas = [];
var mapster_options = {
    mapKey: 'data-name',
    singleSelect: false, // true for only 1 active
    clickNavigate: false,
    //toolTipClose: ['area-mouseout'],
    //toolTipClose: ['area-click'],     // Doesn't work
    toolTipClose: ['tooltip-click'],  // Best option
    //toolTipClose: ['image-mouseout'], // Sometimes it doesn't let you click
    stroke: true,
    strokeWidth: 3,
    staticState: true,
    fillColor: 'c6a344',
    fillOpacity: 0.7,
    strokeColor: 'c6a344',
    showToolTip: false,
    render_select: {
        fillOpacity: 0.5,
        strokeWidth: 2
    },
    onClick: function(data) {
        selectedKey = data;
    },
    //toolTipContainer: $('#treat').html(),
    areas: areas
};

function getBlueprint(coords) {
//    $("#map").html('');
//    $("#map_img").off('click');
    $("#map_img").css('z-index', '0');

//    $("#map_img").attr('src', 'devices/static/assets/img/floors/estga_map.jpg');

	var coord0 = "380,600,20"; // circle (monobloco TI)
	var coord0 = "640,300,20"; // circle (sala 10)

    $("#mymap").append('<area style="display:block;" data-name="AK" coords="'+coord0+'" shape="rect" data-full="teste1" href="javascript:void(0)" />');

    $('#map_img').mapster(mapster_options);
//     $('#map_img')
//        .mapster({
//            mapKey: 'data-key'
//        })
//        .mapster('set',true,'AK');

	console.log(coords);

//	coords.forEach(function(coord) {
//	    console.log('coord',coord);
//		$("#map").append('<area style="display: block;" data-name="'+coord.idDevice+'" shape="rect" coords="'+coord0+'" shape="rect" data-full="teste'+coord.idDevice+'" onclick="javascript:openDevice('+coord.idDevice+')" href="javascript:void(0)" />');
//
//		//areas += '{"key":"'+ i + '", "toolTip":"' + treat_tooltip +'"}';
//		areas.push({
//		   key: device.idDevice.toString(),
//		   toolTip: treat_tooltip
//		});
//	});
//	$('#map_img').mapster(mapster_options);

//	mapster_options['toolTipContainer'] = areas;
}
function GetCoordinates(imgID) {
  var myImg = document.getElementById(imgID);

  var PosX = 0;
  var PosY = 0;
  var ImgPos;
  ImgPos = FindPosition(myImg);

  if (!e) var e = window.event;
  if (e.pageX || e.pageY) {
      PosX = e.pageX;
      PosY = e.pageY;
  }
  else if (e.clientX || e.clientY){
      PosX = e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
      PosY = e.clientY + document.body.scrollTop + document.documentElement.scrollTop;
  }
  PosX = PosX - ImgPos[0];
  PosY = PosY - ImgPos[1];

  console.log('x:', PosX)
  console.log('y:', PosY)
}
function FindPosition(oElement) {
  if(typeof( oElement.offsetParent ) != "undefined")
  {
    for(var posX = 0, posY = 0; oElement; oElement = oElement.offsetParent)
    {
      posX += oElement.offsetLeft;
      posY += oElement.offsetTop;
    }
      return [ posX, posY ];
    }
    else
    {
      return [ oElement.x, oElement.y ];
    }
}