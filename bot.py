#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
import json
from secret import TOKEN

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def _dictToString(dict):
  return str(dict).replace(', ','\r\n').replace("u'","").replace("'","")[1:-1]

def register(update, context):
    """registers a play in the score_board.json
        ex score_board = {
                        "Game": {
                            "gamer1": score
                            "gamer2": score
                             }
                        }
    """

    default = {
        "Zoe": 0,
        "Marce": 0
    }

    # Loads the previous data into our dict
    with open('score_board.json') as json_file:
        score_board = json.load(json_file)

    parameters = update.message.text.split()
    game = parameters[1].capitalize()
    winner = parameters[2].capitalize()

    if game in score_board:
        score_board[game][winner] = score_board[game][winner] + 1
    else:
        score_board[game] = default
        score_board[game][winner] = 1

    # Saved modified dict to the file
    with open("score_board.json", "w") as jsonFile:
        json.dump(score_board, jsonFile)

    update.message.reply_text(game)
    update.message.reply_text(_dictToString(score_board[game]))

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("register", register))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
