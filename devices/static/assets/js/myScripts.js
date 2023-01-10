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

function getInfo() {
    // JQuery
    $('.device-card').each(function(device) {
        let deviceID = $(this).attr('device');
//        console.log('device',device);
//        console.log(deviceID);

//        var interv = window.setInterval( function() {
//          console.log('teste');
//        }, 1000);

//        $.ajax({
//            url: 'http://127.0.0.1:8000/devices/external/getinfo/'+deviceID,
//            type: 'GET',
//            success: function(result) {
//                console.log(result);
//                showNotification('top','center','tim-icons icon-sound-wave','success','Success');

//                $(this).find("#device_temp").text(ramdom);
//                $(this).find("#device_cpu").text(ramdom);
//                $(this).find("#device_mem").text(ramdom);
//            },
//            error: function(XMLHttpRequest, textStatus, errorThrown) {
//                console.log("Status: " + textStatus + "\nError: " + errorThrown);
//                showNotification('top','center','tim-icons icon-sound-wave','danger','Connection Failed');
//            }
//        });

        let ramdom = Math.floor(Math.random() * 10);
        $(this).find("#device_temp").text(ramdom);
        $(this).find("#device_cpu").text(ramdom);
        $(this).find("#device_mem").text(ramdom);

//        clearTimeout(interv);
    });


}
function switch_on_api(id) {
    $.ajax({
        url: 'http://127.0.0.1:8000/devices/external/switch_on/'+id,
        type: 'GET',
        success: function(data) {
            showNotification('top','center','tim-icons icon-check-2','success','Switch on successful');
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            showNotification('top','center','tim-icons icon-sound-wave','danger','Failed: '+errorThrown);
        }
    });
}
function switch_off_api(id) {
    $.ajax({
        url: 'http://127.0.0.1:8000/devices/external/switch_off/'+id,
        type: 'GET',
        success: function(data){
            showNotification('top','center','tim-icons icon-check-2','success','Switch off successful');
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
            showNotification('top','center','tim-icons icon-check-2','success','Switch off successful');
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