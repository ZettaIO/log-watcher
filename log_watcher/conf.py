from __future__ import print_function
import os
import json


def parse_patterns(data):
    print(data)
    try:
        return json.loads(data)
    except Exception as ex:
        print(ex)
        print("Failed to parse WATCHER_PATTERNS:", data)
        raise


class Config(object):
    log_file = os.environ.get("WATCHER_LOG_FILE")
    phone_number = os.environ.get("WATCHER_PHONE_NUMBER")
    message = os.environ.get('WATCHER_PHONE_MESSAGE') or "Poke!"
    patterns = os.environ.get("WATCHER_PATTERNS")

    # These are required
    sms_key = os.environ['SMS_KEY']
    sms_secret = os.environ['SMS_SECRET']

    @classmethod
    def apply(cls, **kwargs):
        cls.log_file = kwargs.get('log_file') or cls.log_file
        cls.patterns = parse_patterns(kwargs.get('patterns') or cls.patterns)
        cls.phone_number = kwargs.get('phone_numbers') or cls.phone_number
        cls.message = kwargs.get('message') or cls.message


config = Config()
