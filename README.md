# log-watcher

A small tool use to watch for rare events in log files
sending an alert immediately. An sms is sent using
gatewayapi.com.

This project was created in a hurry, so don't have high expectations!

## Env vars

```bash
# Full path to the log file to watch
WATCHER_LOG_FILE
# Pattern in log file to look for
WATCHER_PATTERN
# Phone number (sms). Must be in format 00<country-code><number>
WATCHER_PHONE_NUMBER
# The message to send
WATCHER_PHONE_MESSAGE

# gatewayapi.com api account
SMS_SECRET
SMS_KEY
```
