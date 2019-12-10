import os
import time
import traceback
import threading
import inotify.adapters
from log_watcher import config, sms


def process(line, history=False):
    if config.pattern:
        if config.pattern in line:
            sms.send()


def follow(config, from_beginning=False):    
    notifier = inotify.adapters.Inotify()
    logfile = config.log_file.encode()

    while True:
        try:
            # Check if logfile exists
            if not os.path.exists(logfile):
                print 'logfile does not exist'
                time.sleep(1)
                continue
                print 'opening and starting to watch', logfile

            # Open the file and read it from the beginning or end
            file = open(logfile, 'r')
            if from_beginning:
                for line in file.readlines():
                    process(line, history=True)
                else:
                    file.seek(0, 2)
                    from_beginning = True

            # Watch for file events and react
            notifier.add_watch(logfile)
            try:
                for event in notifier.event_gen():
                    if event is not None:
                        (header, type_names, watch_path, filename) = event
                        if set(type_names) & set(['IN_MOVE_SELF']): # moved
                            print 'logfile moved'
                            notifier.remove_watch(logfile)
                            file.close()
                            time.sleep(1)
                            break
                        elif set(type_names) & set(['IN_MODIFY']): # modified
                            for line in file.readlines():
                                process(line, history=False)
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                notifier.remove_watch(logfile)
                file.close()
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            break
        except inotify.calls.InotifyError:
            time.sleep(1)
        except IOError:
            time.sleep(1)
        except:
            traceback.print_exc()
            time.sleep(1)
