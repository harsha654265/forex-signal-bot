import time
import requests

TOKEN = "8135553631:AAEez0VrglZoZSiXDV1QrhWUfGnXOLcocWs"
CHAT_ID = "7671074142"

def send_telegram_signal(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)
    
