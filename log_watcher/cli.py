import os
import sys
import argparse

from log_watcher import config, sms, watcher


def main():
    """cli entrypoint"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'action',
        choices=['watch', 'test-sms'],
    )
    parser.add_argument(
        '--log-file',
        help="The log file to watch",
    )
    parser.add_argument(
        '--pattern',
        help="The pattern to detect",
    )
    parser.add_argument(
        '--phone-number',
        help="The phone number to nag (sms)"
    )
    parser.add_argument(
        '--message',
        help="The message to send"
    )
    values = parser.parse_args(sys.argv[1:])

    # Fall back to env vars if needed
    config.apply(
        log_file=values.log_file,
        pattern=values.pattern,
        phone_number=values.phone_number,
        message=values.message,
    )

    if values.action == 'test-sms':
        sms.send()

    if values.action == 'watch':
        watcher.follow(config, from_beginning=False)
