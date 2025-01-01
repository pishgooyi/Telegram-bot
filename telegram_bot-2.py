
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define your bot's token here
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Define a start command function
def start(update, context):
    update.message.reply_text("Hello! I am your bot. How can I help you today?")

# Define a message handler function
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command and message handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
