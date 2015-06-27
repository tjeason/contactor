$(document).ready(function() {
  $('#send').click(function(event) {
    var name = $('#NAME').val(),
        email = $('#EMAIL').val(),
        msg = $('#MSG').val();

    $.ajax({
      type: 'POST',
      url: 'http://localhost:9000/md/send',
      data: {
        'fromName': name,
        'fromEmail': email,
        'msg': msg,
        'subject': 'New Contact Message',
        'toEmail': 'support@company.com',
        'toName': 'Support'
      }
     }).done(function(response) {
      console.log(response);
    });

    event.preventDefault();

  });
});
