#!/usr/bin/env python
# File: mailgunner.py

import os
import requests
import time

from log import logColor

DOMAIN_NAME = os.environ.get('MAILGUN_DOMAIN_NAME')
API_KEY = os.environ.get('MAILGUN_API_KEY')

class MailGunHandler:
    # Send a plain text message.
    def send_simple_message(self, from_name, from_email, to_name, to_email, subject, message):
        print logColor.INFO + "[", time.asctime(), "] Sending contact message through Mailgun." + logColor.END

        url = "https://api.mailgun.net/v3/%s/messages" % DOMAIN_NAME

        return requests.post(
            url,
            auth=("api", API_KEY),
            data={"from": from_email,
                  "to": [to_email],
                  "subject": subject,
                  "text": message})
