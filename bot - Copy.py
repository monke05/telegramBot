import logging
import flask, requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update,Bot

logging.basicConfig(format='%(asctime)s - %(name)s -%(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = ""



def start(bot,update):
    print(update)
    author = update.message.from_user.first_name
    reply = f"Hi! {author}"
    bot.send_message(chat_id=update.message.chat_id,text=reply)

def _help(bot,update):
    help_text = "i am a very helpfull help text"
    bot.send_message(chat_id=update.message.chat_id,text=help_text)

def echo_text(bot,update):
    reply = update.message.text
    bot.send_message(chat_id=update.message.chat_id,text=reply)
 
def echo_sticker(update: Update, context: CallbackContext):
    bot.send_sticker(chat_id=update.message.chat_id , sticker=update.message.sticker.file_id)

def error(bot,update):
    logger.error(f"Update {update} caused error {update.error}")



def main():
    updater = Updater(TOKEN,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",_help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()





if (__name__ == "__main__"):
    main()













# def message_handler(update: Update,context: CallbackContext):
#     text = update.to_dict()['message']['text']
#     update.message.reply_text(text)

# def greeting(update: Update,context: CallbackContext):
#     first_name = update.to_dict()['message']['chat']['first_name']
#     # logger.info(first_name)
# ##    print(update.to_dict().keys(),first_name)
#     update.message.reply_text("hi {}".format(first_name))