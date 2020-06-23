import configparser
import logging

import telegram
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters



# Load data from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Initial Flask app
app = Flask(__name__)

# Initial bot by Telegram access token
bot = telegram.Bot(token=(config['TELEGRAM']['ACCESS_TOKEN']))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        
        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
    return 'ok'

first_meet=True

import subprocess

def reply_handler(bot, update):
    """Reply message."""
    print(bot.getChat(update.message.chat_id))
    username = bot.getChat(update.message.chat_id)['username']
    user_id = str(bot.getChat(update.message.chat_id)['id'])
    user_cmd = update.message.text
    
    #text = update.message.text
   
    re = []
    
    
    try:
        os.popen("docker run --name "+user_id+" -it test:1.0").read()
    except:
        print("==already exist")
    command = "docker start " + user_id + " && docker exec -it "+ user_id + " bash -c \""+  user_cmd+" \""
  
    output = os.popen(command).read()
    out = output.split()
    print('===',out)

    
    out.pop(0)
    msg = '\n'.join(map(str, out))
    if msg=="":
        msg = os.popen("docker exec -it "+ user_id  +" ls").read()
    else:
        out.pop()
        


    output = os.popen("docker stop "+user_id).read()
    if user_cmd == '/start':
        msg = username+'您好！歡迎使用Terrrrminal!'
         
    update.message.reply_text(msg)


# New a dispatcher for bot
dispatcher = Dispatcher(bot, None)

# Add handler for handling message, there are many kinds of message. For this handler, it particular handle text
# message.
dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))



import os

if __name__ == "__main__":
    # Running server
    
    app.run(debug=True)