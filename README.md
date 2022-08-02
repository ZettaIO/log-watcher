# log-watcher

A small tool for monitoring service logs in journald
looking for rare evens sending an alert immediately.
An sms is sent using gatewayapi.com.

This project was created in a hurry, so don't have high expectations!

Note that version 1 simpy read log files directly trying
to follow log rotation using inotify.

## Supported python version

* Python 3.7

## Install

cysystemd

Binary wheels can be found here:
https://github.com/mosquito/cysystemd/releases/

installing from source:

```
sudo apt install build-essential libsystemd-dev
pip install cysystemd
```

## Env vars

```bash
# The service name to watch in journald
WATCHER_SERVICE_NAME="dockerd"
# Pattern in log file to look for
WATCHER_PATTERNS='["some pattern", "another pattern"]'
# Phone number (sms). Must be in format 00<country-code><number>
WATCHER_PHONE_NUMBER=004700000000
# The message to send
WATCHER_PHONE_MESSAGE="Halp!"

# gatewayapi.com api account
SMS_SECRET
SMS_KEY
```
