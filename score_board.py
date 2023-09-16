from telegram.ext import CommandHandler, filters
import logging
import json

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def _dictToString(dicto):
  if dicto:
    return str(dicto).replace(', ','\r\n').replace('}','\r\n').replace("u'","").replace("'","").replace(': {','\r\n')[1:-1]
  else:
    return "No hay partidas."


async def register_game(update, context):
    logger.info(f'Registered Game command by {update.message.from_user.username}')

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
    if len(parameters) <2:
        await context.bot.send_message(
                    chat_id=update.message.chat_id,
                     text="Nope, es /partida nombre_juego  ganadore")
        return
        

    game = parameters[1].capitalize()
    winner = parameters[2].capitalize()
    if winner not in default.keys():
        await context.bot.send_message(
                    chat_id=update.message.chat_id,
                     text="No te conozco...")
        return

    if game in score_board:
        score_board[game][winner] = score_board[game][winner] + 1
    else:
        score_board[game] = default
        score_board[game][winner] = 1

    # Saved modified dict to the file
    with open("score_board.json", "w") as jsonFile:
        json.dump(score_board, jsonFile)

    await context.bot.send_message(
                    chat_id=update.message.chat_id,
                     text=game + '\r\n' + _dictToString(score_board[game]))

async def show_score_board(update, context):
    logger.info(f'Show Board command by {update.message.from_user.username}')

    with open('score_board.json') as json_file:
        score_board = json.load(json_file)

    await context.bot.send_message(
                    chat_id=update.message.chat_id,
                     text=_dictToString(score_board))

async def delete_game(update, context):
    logger.info(f'Delete Game command by {update.message.from_user.username}')

    with open('score_board.json') as json_file:
        score_board = json.load(json_file)
    parameters = update.message.text.split()
    if len(parameters) <2:
        await context.bot.send_message(
                    chat_id=update.message.chat_id,
                     text="Nope, es  /borrar_juego nombre_juego")
        return
        
    game = parameters[1].capitalize()
    if game not in score_board.keys():
        await context.bot.send_message(
                    chat_id=update.message.chat_id,
                     text="No existe ese juego.")

    score_board.pop(game,None)

    with open("score_board.json", "w") as jsonFile:
        json.dump(score_board, jsonFile)
    show_score_board(update,context)

def set_handlers(application):

    application.add_handler(CommandHandler("partida", register_game))
    application.add_handler(CommandHandler("como_vamos", show_score_board))
    application.add_handler(CommandHandler("borrar_juego", delete_game))
