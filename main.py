import telegram.ext
from telegram.ext import *
import chat_Model as CM

print('STARTING BOT...')

TOKEN = '2146711246:AAGjdz8ruMv9fVlMTeBaFnDRP6t9E-2DF0c'

updater = telegram.ext.Updater(TOKEN, use_context=True)
dp = updater.dispatcher
def start(update, context):
    update.message.reply_text("""
    Write your destination, the time you want to spend there, and the number of people. 😉
    """)

def handle_message(update, context):
    text = str(update.message.text).lower()
    update.message.reply_text(CM.reply(text))

dp.add_handler(telegram.ext.CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, handle_message))
updater.start_polling()
updater.idle()
