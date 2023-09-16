from telegram.ext import CommandHandler, filters
import logging
import json
import secrets

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def choose_mock():
    foo = ['loooooseeeeerrrrr',
           'jaaaaa pelotudo', 
           'try again next time', 
           'sssssssss', 
           'te quiero aunque seas un perdedor cronico',]
    
    return secrets.choice(foo)


async def mock_player(update, context):
    logger.info(f'Mock Player command by {update.message.from_user.username}')
    # Loads the previous data into our dict
    with open('users.json') as json_file:
        users = json.load(json_file)
    
    parameters = update.message.text.split()
    if len(parameters) <2:
        await context.bot.send_message(
                    chat_id=update.message.chat_id,
                     text="Nope, es /burlarse username_jugador")
        return 
    
    mocked = parameters[1].replace('@','')
    if mocked not in list(users.keys()):
        await context.bot.send_message(
                    chat_id=update.message.chat_id,
                     text="No le conozco...")
        return

  
    await context.bot.send_message(
                    chat_id=users[mocked]['chat_id'],
                    text=f'{update.message.from_user.username} activated MOCK PROTOCOL: \n {choose_mock()}')


async def ping_player(update, context):
    logger.info(f'Ping Player command by {update.message.from_user.username}')
    # Loads the previous data into our dict
    with open('users.json') as json_file:
        users = json.load(json_file)
    
    parameters = update.message.text.split()
    if len(parameters) <2:
        await context.bot.send_message(
                    chat_id=update.message.chat_id,
                     text="Nope, es /burlarse username_jugador")
        return 
    
    mocked = parameters[1].replace('@','')
    if mocked not in list(users.keys()):
        await context.bot.send_message(
                    chat_id=update.message.chat_id,
                     text="No le conozco...")
        return

  
    await context.bot.send_message(
                    chat_id=users[mocked]['chat_id'],
                    text=f'🟦')



def set_handlers(application):

    application.add_handler(CommandHandler("burlarse", mock_player))
    application.add_handler(CommandHandler("ping", ping_player))