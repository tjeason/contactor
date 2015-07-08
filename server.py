#!/usr/bin/env python
# File: server.py

import BaseHTTPServer
import cgi
import SimpleHTTPServer
import sys
import time
from mailgunner import MailGunHandler
from mandriller import MandrillHandler
from log import logColor

ServerClass = BaseHTTPServer.HTTPServer

# HTTP requests handler.
class ContactorRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            print logColor.INFO + "[", time.asctime(), "] INFO: Getting index page." + logColor.END
            self.path = '/content/index.html'

        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

        if ctype == 'multipart/form-data':
            post_vars = cgi.parse_multipart(self.rfile, pdict)

        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            post_vars = cgi.parse_qs(self.rfile.read(length), keep_blank_values = 1)

        else:
            post_vars = {}

        # Parse values from post_vars
        if len(post_vars) > 0:
            from_name = post_vars.get('fromName', [''])[0]
            from_email = post_vars.get('fromEmail', [''])[0]
            to_name = post_vars.get('toName', [''])[0]
            to_email = post_vars.get('toEmail', [''])[0]
            subject = post_vars.get('subject', [''])[0]
            message = post_vars.get('msg', [''])[0]
            attachment = post_vars.get('attachment', [''])[0]

            # Mandrill API is sending the contact information.
            if self.path == '/md/send':
                print logColor.INFO + "[", time.asctime(), "] INFO: Received Mandrill POST request." + logColor.END
                MandrillHandler().send_simple_message(from_name, from_email, to_name, to_email, subject, message)

            # Mailgun is sending the contact information.
            if self.path == '/mg/send':
                print logColor.INFO + "[", time.asctime(), "] INFO: Received Mailgun POST request. Sending message..." + logColor.END
                MailGunHandler().send_simple_message(from_name, from_email, to_name, to_email, subject, message)

            if self.path == '/mg/send/file':
                print logColor.INFO + "[", time.asctime(), "] INFO: Received Mailgun POST request. Sending message with file attached..." + logColor.END
                MailGunHandler().send_complex_message(from_name, from_email, to_email, subject, message, attachment)

        # At least some contact form data is missing.
        else:
            print logColor.ERROR + "[", time.asctime(), "] ERROR: Could not retrieve contact information." + logColor.END

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        return

def showIntro():
    intro = """
        _________                __                 __
        \_   ___ \  ____   _____/  |______    _____/  |_  _____________
        /    \  \/ /  _ \ /    \   __\__  \ _/ ___\   __\/  _ \_  __  /
        \     \___(  <_> )   |  \  |  / __ \  \___|  | (  <_> )  |  \/
         \______  /\____/|___|  /__| (____  /\___  >__|  \____/|__|
                \/            \/          \/     \/
    """
    print logColor.OKBLUE + intro + logColor.END

if __name__ == "__main__":
    try:
        if sys.argv[1:]:
            port = int(sys.argv[1])

        else:
            port = 9000

        server_address = ('0.0.0.0', port)

        Handler = ContactorRequestHandler
        httpd = ServerClass(server_address, Handler)
        serv = httpd.socket.getsockname()
        showIntro()
        print logColor.INFO + "[", time.asctime(), "] INFO: Serving running on", serv[0], "using port", serv[1], "..." + logColor.END
        httpd.serve_forever()

    except KeyboardInterrupt:
        print logColor.WARN + "[", time.asctime(), "] WARN: Server shutting down." + logColor.END
        httpd.socket.close()
