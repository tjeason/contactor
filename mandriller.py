#!/usr/bin/env python
# File: mandriller.py

import os
import time
import mandrill
from log import logColor

API_KEY = os.environ.get('MANDRILL_API_KEY')
mandrill_client = None

# Check if Mandril API Key exists in environment variable.
if API_KEY != None:
    print '++++ API_KEY: ', API_KEY
    mandrill_client = mandrill.Mandrill(API_KEY)

# Raise warning message.
else:
    print logColor.WARN + "[", time.asctime(), "] Could not find your Mandrill API key. Make sure you have it assigned as an ENV $MANDRILL_API_KEY" + logColor.END

class MandrillHandler:
    # Send a plain text message.
    def send_simple_message(self, from_name, from_email, to_name, to_email, subject, msg):
        print logColor.INFO + "[", time.asctime(), "] Sending contact message through Mandrill." + logColor.END

        try:
            message = {
                'auto_html': None,
                'auto_text': None,
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
            result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool', send_at=None)

        except mandrill.Error, e:
            # Mandrill errors are thrown as exceptions
            print logColor.ERROR + "A mandrill error occurred: %s - %s" % (e.__class__, e) + logColor.END
            raise
