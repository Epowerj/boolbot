
from telegram.ext import Updater
import logging
from key import apikey
import boolio

users = []

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

def register_user(bot, update):
    if update.message.from_user.id not in users:
        users[update.message.from_user.id] = [] #add dict of booleans


def isregistered(chatid):
    return chatid in users

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')
    register_user(bot, update)


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Just ask @Epowerj')


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def new(bot, update):
    # make a bool and save it
    b = boolio.Bool()
    print(b.bid)
    print(b.val)  # ???, False
    b(True)
    print(b.bid)
    print(b.val)  # ???, True
    #boolio.save('important_flag.bool', b)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(apikey)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", help)
    dp.addTelegramCommandHandler("new", new)

    # on noncommand i.e message - echo the message on Telegram -- dp.addTelegramMessageHandler(echo)

    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()