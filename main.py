import telegram.ext
from telegram.ext import *
import model

print('STARTING BOT...')

TOKEN = '---------------> BOT TOKEN <---------------'

updater = telegram.ext.Updater(TOKEN, use_context=True)
dp = updater.dispatcher
def start(update, context):
    update.message.reply_text("Write your destination, the time you want to spend there, and the number of people. 😉")

def handle_message(update, context):
    text = str(update.message.text).lower()
    reply_message = model.chat_with_model(text, model.conversation,model.chatbot_prompt)
    update.message.reply_text(reply_message)

dp.add_handler(telegram.ext.CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, handle_message))
updater.start_polling()
updater.idle()
