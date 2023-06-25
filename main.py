#pip install python-telegram-bot==13.3
import re
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Telegram bot token (obtained from BotFather)
TOKEN = 'token'

# Pattern to match for notifications (change it according to your needs)
pattern = r"Update"

# Function to handle new messages
def handle_message(update, context):
    message = update.message.text
    if re.search(pattern, message):
        # Trigger your notification mechanism here (e.g., send an email, push notification, etc.)
        print("New message matching pattern:", message)

# Create the Telegram Updater and dispatcher
updater = Updater(token=TOKEN,use_context=True)
dispatcher = updater.dispatcher

# Set up the message handler
message_handler = MessageHandler(Filters.text, handle_message)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
