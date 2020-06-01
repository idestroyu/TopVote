function handleCloseAlert(alert) {
    $.ajax({
        type: "post",
        url: "/alerts/seen",
        data: {"alert_id": alert.id}
    }).done(function(data) {
        alert.parentElement.remove();
    }).fail(function(data) {
    });
}