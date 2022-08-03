import time
from cysystemd.reader import (
    JournalReader,
    JournalOpenMode,
    Rule,
)
from log_watcher import sms

# Use some sane send cooldown
sms_last_sent = 0
sms_cooldown = 10


def follow(config, from_beginning=False, poll_timeout=255):
    """Continiously read from journald"""
    global sms_last_sent
    reader = JournalReader()
    reader.open(JournalOpenMode.SYSTEM)
    reader.add_filter(Rule("_SYSTEMD_UNIT", config.service_name))
    if from_beginning:
        reader.seek_head()
    else:
        reader.seek_tail()

    while True:
        reader.wait(poll_timeout)

        for record in reader:
            # print(record.date, record.data["MESSAGE"])
            # print(str(record.data))

            for pattern in config.patterns:
                if pattern in record.data["MESSAGE"]:
                    if time.time() - sms_last_sent > sms_cooldown:
                        sms.send()
                        sms_last_sent = time.time()
                    # Avoid spamming multiple messages
                    break
