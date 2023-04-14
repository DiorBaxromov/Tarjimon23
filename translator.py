import os
import telegram

from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from googletrans import Translator
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

updater = Updater(token=TOKEN)

def start(update, context):
    user = update.message.from_user.first_name
    update.message.reply_html(f'Welcome <b>{user}</b> ❤️')


def receive_and_send(update, context):
    """получает текст от ползователей переводит и отправляет обратно"""
    chat = update.effective_chat
    message = update.message.text
    perevod = text_translate(text=message, src='en', dest='ru')
    context.bot.send_message(chat_id=chat.id, text=perevod)


def text_translate(text, src, dest):
    """переводит текст"""
    try:
        translator = Translator()
        translation = translator.translate(text=text, src=src, dest=dest)
        return translation.text
    except Exception as ex:
        return ex

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, receive_and_send))
updater.start_polling()
updater.idle()
