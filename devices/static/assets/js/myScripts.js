function switch_on_api(id) {
    $.get('http://127.0.0.1:8000/devices/external/switch_on/'+id, function () {
        showNotification('top','center','tim-icons icon-check-2','success','Switch on successful');
    });
}
function switch_off_api(id) {
    $.get('http://127.0.0.1:8000/devices/external/switch_off/'+id, function () {
        showNotification('top','center','tim-icons icon-check-2','success','Switch off successful');
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

    $.ajax({
        url: 'http://127.0.0.1:8000/api/devices/'+id+'/update',
        type: 'PUT',
        data: obj,
        success: function(result) {
            console.log(result);
            showNotification('top','center','tim-icons icon-check-2','success','Edited successful');
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
