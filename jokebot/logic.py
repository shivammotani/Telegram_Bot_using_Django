import json
from telegram.ext import *
from telegram import *
import random 

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

buttons = [
    [
        InlineKeyboardButton(text="Stupid",callback_data = "Stupid"),
        InlineKeyboardButton(text="Dumb",callback_data = "Dumb"),
        InlineKeyboardButton(text="Fat",callback_data = "Fat")
    ]
  ]
keyboard = InlineKeyboardMarkup(buttons)


def msgToBeSent(chat_id, msg):
    return ["sendMessage", {
          'chat_id': chat_id,
          'text': msg,
          'reply_markup': json.dumps(eval(str(keyboard)))
        }]

def buttons(update):
  chat_id = update['message']['chat']['id']
  return msgToBeSent(chat_id, 'Choose from the following')


def handle_update(update):
  chat_id = update['callback_query']['from']['id']
  text = update['callback_query']['data'].lower()

  if(text == 'stupid'):
    msg = random.choice(jokes['stupid'])
    return msgToBeSent(chat_id, msg)

  elif(text == 'fat'):
    msg = random.choice(jokes['fat'])
    return msgToBeSent(chat_id, msg)

  else:
    msg = random.choice(jokes['dumb'])
    return msgToBeSent(chat_id, msg)
