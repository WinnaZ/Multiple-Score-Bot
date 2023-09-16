#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
from secret import TOKEN
from telegram.ext import Application, MessageHandler, filters
import score_board, base, party_tricks
import logging
logger = logging.getLogger(__name__)


async def unknown_command(update, context):
    text = "No reconozco el comando, para ver comandos válidos usá /ayuda"
    await context.bot.send_message(chat_id=update.message.chat_id, text=text)

def set_handlers(application):
    base.set_handlers(application)
    score_board.set_handlers(application)
    party_tricks.set_handlers(application)

if __name__ == '__main__':
    logger.info('Starting Bot')

    application = Application.builder().token(TOKEN).build()
    set_handlers(application)
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    application.run_polling()
