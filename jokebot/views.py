from django.shortcuts import render
from .models import noOfCalls
from telegram.ext import *
from telegram import *
import random
from jokebot.models import *
from jokebot.databaseUpdate import *
# Create your views here.

jokes = {
         'stupid': ["""What did one ocean say to another? --> Nothing, they just waved.""",
                    """Why did the picture get arrested? --> It got framed.""",
                    """What is the name of the penguin’s favorite aunt? --> Aunt Arctica""",
                    """What do you call a bear without ears? --> B""",
                    """What did one wall say to another? --> See you at the corner"""],
         'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                    """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """,
                    """Yo Mama so fat, She wore a yellow raincoat and people yelled Taxi!""",
                    """Yo Mama so fat, She took her pants to the dry cleaners and the lady said, "we don't do curtains.""",
                    """Yo Mama is so fat, I took a picture of her last Christmas and its still printing."""],
         'dumb':   ["""What did one toilet say to the other? --> You look a bit flushed.""",
                    """Why did the tomato blush? --> Because it saw the salad dressing.""",
                    """What did one plate whisper to the other plate? --> Dinner is on me.""",
                    """What do you give a sick lemon? --> A Lemon-aid.""",
                    """Why can’t you trust atoms? --> They make up everything."""] }
    


API_KEY = '<your_botapi_key>'

print('Bot started')

def index(request):
    obj = noOfCalls.objects.all()
    context ={
        "obj":obj,
        }
    return render(request, "index.html",context)

def handle_message(update, context):
    text = str(update.message.text).lower()
    updateDb(update.message.chat_id,text)
    if(text == 'stupid'):
        msg = random.choice(jokes['stupid'])
        update.message.reply_text(msg)
    elif(text == 'fat'):
        msg = random.choice(jokes['fat'])
        update.message.reply_text(msg)
    elif(text == 'dumb'):
        msg = random.choice(jokes['dumb'])
        update.message.reply_text(msg)
    else:
        update.message.reply_text(f"Please select only from the buttons given below:")
    return

def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton("Stupid")],[KeyboardButton("Fat")],[KeyboardButton("Dumb")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text = "Welcome to the bot",
                             reply_markup=ReplyKeyboardMarkup(buttons))



updater = Updater(API_KEY,use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", startCommand))
dp.add_handler(MessageHandler(Filters.text, handle_message))

updater.start_polling(1.0)
