from forex_signals import generate_signal
from telegram_bot import send_telegram_message
from config import CHAT_ID

def main():
    signal = generate_signal()
    if signal:
        send_telegram_message(CHAT_ID, signal)

if __name__ == "__main__":
    main()