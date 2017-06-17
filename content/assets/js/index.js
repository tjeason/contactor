$(document).ready(function() {
  $('#send').submit(function(event) {

    var form = $(this);
    console.log(form);
    var formData = new FormData(document.forms.namedItem("data"));

    console.log(formData);
/*
    $.ajax({
      type: 'POST',
      url: 'http://localhost:9000/mg/send/file',
      data: formData,
      async: true,
        success: function (data) {
          alert(data)
        },
        cache: false,
        processData: false
     }).done(function(response) {
      console.log(response);
    });
*/
    event.preventDefault();

  });
});
