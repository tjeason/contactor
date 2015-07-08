#!/usr/bin/env python
# File: mailgunner.py

import os
import requests
import time

from log import logColor

class MailGunHandler:

    def __init__(self):
        self.API_KEY = os.environ.get('MAILGUN_API_KEY')
        self.DOMAIN_NAME = os.environ.get('MAILGUN_DOMAIN_NAME')

    # Send a plain text message.
    def send_simple_message(self, from_name, from_email, to_name, to_email, subject, message):
        print logColor.INFO + "[", time.asctime(), "] INFO: Sending contact message through Mailgun." + logColor.END

        url = "https://api.mailgun.net/v3/%s/messages" % self.DOMAIN_NAME

        from_user = from_name + " <" + from_email + ">"

        return requests.post(
            url,
            auth=("api", self.API_KEY),
            data={"from": from_user,
                  "to": [to_name, to_email],
                  "subject": subject,
                  "text": message})
