import time
from telegram_bot import send_telegram_signal

signals = [
    "🔻 SELL Signal for EUR/USD",
    "🔼 BUY Signal for USD/JPY",
    "🔼 BUY Signal for USD/CHF",
    "🔼 BUY Signal for USD/CAD",
    "🔻 SELL Signal for EUR/GBP"
]

while True:
    for signal in signals:
        send_telegram_signal(signal)
        print(f"Sent: {signal}")
        time.sleep(120)  # Wait 2 minutes before sending next signal
