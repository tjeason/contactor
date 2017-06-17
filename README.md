## Contactor

[![Build Status](https://travis-ci.org/tjeason/contactor.svg?branch=master)](https://travis-ci.org/tjeason/contactor)

```
_________                __                 __
   \_   ___ \  ____   _____/  |______    _____/  |_  _____________
   /    \  \/ /  _ \ /    \   __\__  \ _/ ___\   __\/  _ \_  __  /
   \     \___(  <_> )   |  \  |  / __ \  \___|  | (  <_> )  |  \/
    \______  /\____/|___|  /__| (____  /\___  >__|  \____/|__|
           \/            \/          \/     \/

[ Sat Jun 17 15:01:59 2017 ] INFO: Serving running on 0.0.0.0 using port 9000 . Use Control-C to shutdown the server...
[ Sat Jun 17 15:02:19 2017 ] INFO: Getting index page.
127.0.0.1 - - [17/Jun/2017 15:02:19] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/Jun/2017 15:02:19] "GET /content/assets/css/custom.css HTTP/1.1" 200 -
127.0.0.1 - - [17/Jun/2017 15:02:19] "GET /content/assets/js/index.js HTTP/1.1" 200 -
```

A Python-based API server for static websites with contact forms. Contactor supports
Rackspace's Mailgun API service and MailChimp's Mandrill API service.

### Requirements

+ Python 2.7
+ request module (for Mailgun's E-mail Delivery service)
+ mandrill module (for Mandrill's E-mail Delivery service)

### Getting Started

1. Clone or download from the GitHub Repository to your local machine.

```shell
git clone https://github.com/tjeason/contactor.git
```

2. Run the `server.py` script with the port number you would like to use. The default port number is *9000*.

```shell
python server.py <port>
```

3. Setup up the _ENVIRONMENT VARIABLES_ for either Mailgun API or Mandrill (or both)
for your USER API KEYS and DOMAIN NAMES.

| Mailgun | Mandrill |
| ------- | -------- |
| MAILGUN_API_KEY | MANDRILL_API_KEY |
| MAILGUN_DOMAIN_NAME | BCC_EMAIL (Optional) |
| CC_EMAIL (Optional) | |
| BCC_EMAIL (Optional) | |

*Example:*
```shell
export MANDRIL_API_KEY={INSERT API KEY HERE}
```

### Usage
Once the server is running, you are able to perform these requests:

Check if Contactor is running by connecting to the URL in your web browser.

*Example:*
`http://localhost:9000/`

REST API to send a contact form message using Mailgun as a HTTP POST request.

![image](https://user-images.githubusercontent.com/7929408/27255938-6cda390c-536e-11e7-987b-390c2dec5a6d.png)


*Example:*
`http://localhost:9000/mg/send`

REST API to send a contact form message using Mandrill as a HTTP POST request.

*Example:*
`http://localhost:9000/md/send`

A jQuery code snippet that can be used in the `<script>` tag of an HTML file or external JavaScript file.

*Example:*

```javascript

  // Submit button click event handler.
  $('#submit').click(function(event) {
    // Get values from text fields from contact form.
    var name = $('#NAME').val(),
        email = $('#EMAIL').val(),
        msg = $('#MSG').val();

    // Send data to Contactor.
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
```

### Roadmap
 + Heroku deployment setup
 + Send messages with file attachments (WIP)

### License

The MIT License (MIT)

Copyright (c) 2015

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
