import os
import json


def parse_patterns(data):
    try:
        return json.loads(data)
    except Exception as ex:
        print(ex)
        print("Failed to parse WATCHER_PATTERNS:", data)
        raise


class Config(object):
    service_name = os.environ.get("WATCHER_SERVICE_NAME")
    phone_number = os.environ.get("WATCHER_PHONE_NUMBER")
    message = os.environ.get('WATCHER_PHONE_MESSAGE') or "Poke!"
    patterns = os.environ.get("WATCHER_PATTERNS")

    # These are required
    sms_key = os.environ['SMS_KEY']
    sms_secret = os.environ['SMS_SECRET']

    @classmethod
    def apply(cls, **kwargs):
        cls.service_name = kwargs.get('service_name') or cls.service_name
        cls.patterns = parse_patterns(kwargs.get('patterns') or cls.patterns)
        cls.phone_number = kwargs.get('phone_number') or cls.phone_number
        cls.message = kwargs.get('message') or cls.message


config = Config()
