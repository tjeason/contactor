#!/usr/bin/env python
# File: mailgunner.py

import os
import requests
import time

from log import logColor

class MailGunHandler:

    def __init__(self):
        print logColor.INFO + "[", time.asctime(), "] INFO: Getting ENV VARS for Mailgun usage." + logColor.END

        self.API_KEY = os.getenv('MAILGUN_API_KEY')
        self.DOMAIN_NAME = os.getenv('MAILGUN_DOMAIN_NAME')

        if self.API_KEY == None:
            print logColor.ERROR + "[", time.asctime(), "] ERROR: Could not find Mailgun API key. Check your MAILGUN_API_KEY Environment Variable." + logColor.END
            return

        if self.DOMAIN_NAME == None:
            print logColor.ERROR + "[", time.asctime(), "] ERROR: Could not find Mailgun domain name. Check your MAILGUN_DOMAIN_NAME Environment Variable." + logColor.END
            return

        self.CC_EMAIL = os.getenv("CC_EMAIL", '')
        self.BCC_EMAIL = os.getenv("BCC_EMAIL", '')

    # Send a plain text message.
    def send_simple_message(self, from_name, from_email, to_name, to_email, subject, message):
        print logColor.INFO + "[", time.asctime(), "] INFO: Sending contact message through Mailgun." + logColor.END

        from_user = from_name + " <" + from_email + ">"
        url = "https://api.mailgun.net/v3/%s/messages" % self.DOMAIN_NAME

        return requests.post(
            url,
            auth=("api", self.API_KEY),
            data={"from": from_user,
                  "to": [to_name, to_email],
                  "subject": subject,
                  "text": message})

    # Send a message with a file attachment.
    def send_complex_message(self, from_name, from_email, to_email, subject, message, attachment):
        print logColor.INFO + "[", time.asctime(), "] INFO: Sending contact message through Mailgun with attached file." + logColor.END

        from_user = from_name + " <" + from_email + ">"
        url = "https://api.mailgun.net/v3/%s/messages" % self.DOMAIN_NAME

        return requests.post(
            url,
            auth=("api", self.API_KEY),
            files=[("attachment", open(attachment))],
            data={"from": from_user,
                  "to": to_email,
                  "cc": self.CC_EMAIL,
                  "bcc": self.BCC_EMAIL,
                  "subject": subject,
                  "text": message,
                  "html": message})
