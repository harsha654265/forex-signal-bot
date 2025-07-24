from telegram import Bot
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

def send_telegram_message(chat_id, message):
    bot.send_message(chat_id=chat_id, text=message)