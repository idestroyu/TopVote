$( ".register-form" ).submit(function( event ) {
  var form = $(this);
  console.log(form.serialize())
  $.ajax({
    type: "post",
    url: "/user/register",
    data: form.serialize()
  }).done(function(data) {

  }).fail(function(data) {

  });

  event.preventDefault();
});

$( ".login-form" ).submit(function( event ) {
  var form = $(this);
  console.log(form.serialize())
  $.ajax({
    type: "post",
    url: "/user/login",
    data: form.serialize()
  }).done(function(data) {

  }).fail(function(data) {

  });

  event.preventDefault();
});

$( ".create-list-form" ).submit(function( event ) {
  var form = $(this);
  var data = form.serializeArray();
  data.push({name: 'category_id', value: $("#category_id").children("option:selected").attr("id")});
  console.log(form.serialize())
  $.ajax({
    type: "post",
    url: "/lists/create",
    data: data
  }).done(function(data) {

  }).fail(function(data) {

  });

  event.preventDefault();
});