// Mandar formulario para registrarse
$( "#register-form" ).submit(function( event ) {
  var form = $(this);
  console.log(form.serialize())
  $.ajax({
    type: "post",
    url: "/register",
    data: form.serialize()
  }).done(function(data) {
    window.location.href = "/"
  }).fail(function(data) {
        $("#mensaje-error").text(data.responseJSON.message)
        $("#mensaje-error").show()
  });

  event.preventDefault();
});

// Mandar formulario para log in
$( "#login-form" ).submit(function( event ) {
    var form = $(this);
    $.ajax({
        type: "post",
        url: "/login",
        data: form.serialize()
    }).done(function(data) {
        window.location.href = "/"
    }).fail(function(data) {
        $("#mensaje-error").text(data.responseJSON.message)
        $("#mensaje-error").show()
    });

event.preventDefault();
});

// Mandar formulario para crear lista
$( "#create-list-form" ).submit(function( event ) {

  var form = $(this);
  var data = form.serializeArray();

  var formData = new FormData(this);

  formData.append("category_id", $("#category_id").children("option:selected").attr("id"))
  formData.append("elements_file", $('input[type=file]')[0].files[0]);

  console.log(formData.get("elements_file"));
  $.ajax({
    type: "post",
    url: "/lists/create",
    data: formData,
    cache: false,
    contentType: false,
    processData: false,
    enctype: 'multipart/form-data'
  }).done(function(data) {
    window.location.href = "/"
  }).fail(function(data) {

  });

  event.preventDefault();
});

// Mandar formulario para crear elemento
$( "#create-element-form" ).submit(function( event ) {
  var form = $(this);
  var data = form.serializeArray();
  $.ajax({
    type: "post",
    url: "/elements/create",
    data: data
  }).done(function(data) {
    window.location.href = "/lists?id=" + $(".list_id").attr("value")
  }).fail(function(data) {
  });

  event.preventDefault();
});

$( ".boton_votar" ).click(function() {
    var id = $(this).attr("id")
    $.ajax({
        type: "post",
        url: "/elements/vote",
        data: {"elemento_id": id}
    }).done(function(data) {
        window.location.href = "/lists?id=" + $(".list_id").attr("value")
    }).fail(function(data) {
    });
});

$( ".boton_borrar_voto" ).click(function() {
    var id = $(this).attr("id")
    $.ajax({
        type: "delete",
        url: "/elements/deletevote",
        data: {"elemento_id": id}
    }).done(function(data) {
        window.location.href = "/lists?id=" + $(".list_id").attr("value")
    }).fail(function(data) {
    });
});

$(".alert").on("close.bs.alert", function () {
      $alertMsg.hide();
      console.log("HERE")
      return false;
});
