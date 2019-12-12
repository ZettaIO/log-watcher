# log-watcher

A small tool use to watch for rare events in log files
sending an alert immediately. An sms is sent using
gatewayapi.com.

This project was created in a hurry, so don't have high expectations!

## Env vars

```bash
# Full path to the log file to watch
WATCHER_LOG_FILE=full/path/to/log
# Pattern in log file to look for
WATCHER_PATTERNS=["some pattern", "another pattern"]
# Phone number (sms). Must be in format 00<country-code><number>
WATCHER_PHONE_NUMBER=004700000000
# The message to send
WATCHER_PHONE_MESSAGE="Halp!"

# gatewayapi.com api account
SMS_SECRET
SMS_KEY
```
