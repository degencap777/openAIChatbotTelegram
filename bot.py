import telegram.ext
from process import ask, append_interaction_to_chat_log
import logging, os

PORT = int(os.environ.get('PORT', '8443'))
with open('token.txt', 'r') as f:
    TOKEN = str(f.read())

session = {}


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text("Hello! Welcome to KarimHussainBot")


def help(update, context):
    update.message.reply_text("""
    The Following commands are available:
    /start -> Welcome to Karim Hussain
    /help ->This Message
    /about -> About KarimHussain
    /contact -> Developer Info
    
    """)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', context)


def about(update, context):
    update.message.reply_text("""
            KarimHussain is not just a chatbot. Issa lifestyle.
        """)


def contact(update, context):
    update.message.reply_text("Developer: Karim Hussain \n email: test@email.com\n")


def handle_message(update, context):
    chat_log = session.get('chat_log')
    answer = ask(update.message.text, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(update.message.text, answer,
                                                         chat_log)
    update.message.reply_text(f"{str(answer)}")


def main():
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    bot = updater.dispatcher

    bot.add_handler(telegram.ext.CommandHandler("start", start))
    bot.add_handler(telegram.ext.CommandHandler("help", help))
    bot.add_handler(telegram.ext.CommandHandler("about", about))
    bot.add_handler(telegram.ext.CommandHandler("contact", contact))
    bot.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.text, handle_message))

    bot.add_error_handler(error)
    updater.start_polling()

    updater.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path=TOKEN,
        webhook_url='https://karim-hussain.herokuapp.com/' + TOKEN
    )

    updater.idle()


if __name__ == '__main__':
    main()
