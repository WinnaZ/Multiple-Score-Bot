from telegram.ext import CommandHandler, MessageHandler, filters
import logging
import json

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


async def start(update, context):
    """Send a message when the command /start is issued."""
    logger.info(f'Start command by {update.message.from_user.username}')
    with open('users.json') as json_file:
        users = json.load(json_file)
    user = update.message.from_user.username
    if user not in users.keys():
        users[user] = {
            'username':user,
            'chat_id':update.message.chat_id,
            'name': update.message.from_user.first_name,
            'last_name': update.message.from_user.last_name,

        }
        with open("users.json", "w") as jsonFile:
            json.dump(users, jsonFile)

        await context.bot.send_message(
                    chat_id=update.message.chat_id,
                     text='Welcome!')
        return
  
    await context.bot.send_message(
                    chat_id=update.message.chat_id,
                     text='Welcome back!')

async def help(update, context):
    """Send a message when the command /help is issued."""
    logger.info(f'Help command by {update.message.from_user.username}')

    await context.bot.send_message(
            chat_id=update.message.chat_id,
            text="""
            Comandos Disponibles:
            partida - Registra una nueva partida. Formato: /partida nombre_juego  ganadore
            como_vamos - Muestra el puntaje de cada juego.
            borrar_juego - Borra un juego. Formato: /borrar_juego nombre_juego
            burlarse - Se burla de un jugador. Formato: /burlarse username_jugador
            ping - Pingea a otro jugador con un 🟦. Formato: /ping username_jugador 
            """
            )


async def echo(update, context):
    logger.info(f'echo command by {update.message.from_user.username}')
    """Echo the user message."""
    await context.bot.send_message(
                    chat_id=update.message.chat_id,
                    text=update.message.text)


async def error(update, context):
    logger.info(f'error command by {update.message.from_user.username}')

    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def set_handlers(application):

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler("help", help))
    # application.add_error_handler(error)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
