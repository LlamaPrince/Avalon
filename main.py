from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

token = '1207950012:AAGPGpvYVVqtCpGjnn72JD4DWKzmyzLpqYY'

new_lobby_msg = "Ok, %s! I created a lobby for you called %s. Have your friends join it, and then use /start_game when you are ready to play!"

def new_game(update, context):
    text = update.effective_message.text
    if text is None:
      context.bot.send_message(chat_id=update.effective_chat.id, text="Did not recognize non text message")
      return
    args = text.split()
    if len(args) != 3:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Usage: /new_game your_nickname  lobby_name")
        return
    nickname = args[1]
    lobby_name = args[2]
    context.bot.send_message(chat_id=update.effective_chat.id, text=new_lobby_msg % (nickname, lobby_name))

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                 level=logging.INFO)
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    new_game_handler = CommandHandler("new_game", new_game)
    dispatcher.add_handler(new_game_handler)
    updater.start_polling()

main()
