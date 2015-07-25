#!/usr/bin/env python
# File: mandriller.py

import base64
import mandrill
import mimetypes
import os
import time

from log import logColor

class MandrillHandler:

    def __init__(self):
        self.API_KEY = os.getenv('MANDRILL_API_KEY')
        self.BCC_EMAIL = os.getenv("BCC_EMAIL", '')

        self.mandrill_client = None

        # Check if Mandril API Key exists in environment variable.
        if self.API_KEY != None:
            self.mandrill_client = mandrill.Mandrill(self.API_KEY)

        # Raise warning message.
        else:
            print logColor.WARN + "[", time.asctime(), "] INFO: Could not find your Mandrill API key. Make sure you have it assigned as an ENV MANDRILL_API_KEY" + logColor.END

    # Send a plain text message.
    def send_simple_message(self, from_name, from_email, to_name, to_email, subject, msg):
        print logColor.INFO + "[", time.asctime(), "] INFO: Sending contact message through Mandrill." + logColor.END

        try:
            message = {
                'auto_html': None,
                'auto_text': None,
                'bcc_address': self.BCC_EMAIL,
                'from_email': from_email,
                'from_name': from_name,
                'global_merge_vars': [],
                'headers': {'Reply-To': from_email},
                'html': msg,
                'important': False,
                'inline_css': None,
                'merge': True,
                'merge_language': 'mailchimp',
                'preserve_recipients': None,
                'return_path_domain': None,
                'signing_domain': None,
                'subject': subject,
                'tags': ['contact'],
                'text': msg,
                'to': [{'email': to_email,
                     'name': to_name,
                     'type': 'to'}],
                'track_clicks': None,
                'track_opens': None,
                'tracking_domain': None,
                'url_strip_qs': None,
                'view_content_link': None
            }
            self.mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool', send_at=None)

        except mandrill.Error, e:
            # Mandrill errors are thrown as exceptions
            print logColor.ERROR + "[", time.asctime(), "] ERROR: A Mandrill error occurred: %s - %s" % (e.__class__, e) + logColor.END
            raise

    # Send a message with a file attachment.
    def send_complex_message(self, from_name, from_email, to_email, to_name, subject, msg, attachment):
        print logColor.INFO + "[", time.asctime(), "] INFO: Sending contact message through Mandrill with attached file." + logColor.END

        with open(attachment) as attached_file:
            content = base64.b64encode(attached_file.read())

        file_type = mimetypes.guess_type(attachment)[0]

        try:
            message = {
                'attachments': [{'content': content,
                      'name': attachment,
                      'type': file_type}],
                'auto_html': None,
                'auto_text': None,
                'bcc_address': self.BCC_EMAIL,
                'from_email': from_email,
                'from_name': from_name,
                'global_merge_vars': [],
                'headers': {'Reply-To': from_email},
                'html': msg,
                'important': False,
                'inline_css': None,
                'merge': True,
                'merge_language': 'mailchimp',
                'preserve_recipients': None,
                'return_path_domain': None,
                'signing_domain': None,
                'subject': subject,
                'tags': ['contact'],
                'text': msg,
                'to': [{'email': to_email,
                     'name': to_name,
                     'type': 'to'}],
                'track_clicks': None,
                'track_opens': None,
                'tracking_domain': None,
                'url_strip_qs': None,
                'view_content_link': None
            }
            self.mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool', send_at=None)

        except mandrill.Error, e:
            # Mandrill errors are thrown as exceptions
            print logColor.ERROR + "[", time.asctime(), "] ERROR: A mandrill error occurred: %s - %s" % (e.__class__, e) + logColor.END
            raise
