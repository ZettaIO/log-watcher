import os


class Config(object):
    log_file = os.environ.get("WATCHER_LOG_FILE")
    pattern = os.environ.get("WATCHER_PATTERN")
    phone_number = os.environ.get("WATCHER_PHONE_NUMBER")
    message = os.environ['WATCHER_PHONE_MESSAGE'] or "Poke!"

    sms_key = os.environ['SMS_KEY']
    sms_secret = os.environ['SMS_SECRET']

    @classmethod
    def apply(cls, **kwargs):
        cls.log_file = kwargs.get('log_file') or cls.log_file
        cls.pattern = kwargs.get('pattern') or cls.pattern
        cls.phone_number = kwargs.get('phone_numbers') or cls.phone_number
        cls.message = kwargs.get('message') or cls.message


config = Config()
