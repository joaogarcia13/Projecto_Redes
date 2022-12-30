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