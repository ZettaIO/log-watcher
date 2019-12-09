import os
import socket
from requests_oauthlib import OAuth1Session
from log_watcher import config


def send():
    """Send an sms messsage"""
    message = socket.gethostname() + ": " + config.message

    gwapi = OAuth1Session(
        config.sms_key,
        client_secret=config.sms_secret,
    )
    req = {
        'recipients': [{'msisdn': config.phone_number}],
        'message': message,
        'sender': 'Zetta.IO',
    }

    res = gwapi.post('https://gatewayapi.com/rest/mtsms', json=req)
    res.raise_for_status()
