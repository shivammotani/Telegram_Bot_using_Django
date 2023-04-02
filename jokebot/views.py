from django.shortcuts import render
import json
import requests
from django.http import HttpResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from jokebot.cred import TELEGRAM_API_URL
from jokebot.models import *
from jokebot.databaseUpdate import *
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

def index(request):
    obj = noOfCalls.objects.all()
    context ={
        "obj":obj,
        }
    return render(request, "index.html",context)

def send_message(method, data):
  return requests.post(TELEGRAM_API_URL + method, data)


def buttons(update):
  chat_id = update['message']['chat']['id']
  send_message("sendMessage", {
    'chat_id': chat_id,
    'text': 'Choose from the following',
    'reply_markup': json.dumps(eval(str(keyboard)))
  })

def handle_update(update):
  chat_id = update['callback_query']['from']['id']
  text = update['callback_query']['data'].lower()
  updateDb(chat_id,text)
  if(text == 'stupid'):
        msg = random.choice(jokes['stupid'])
        send_message("sendMessage", {
          'chat_id': chat_id,
          'text': msg,
          'reply_markup': json.dumps(eval(str(keyboard)))
        })

  elif(text == 'fat'):
      msg = random.choice(jokes['fat'])
      send_message("sendMessage", {
          'chat_id': chat_id,
          'text': msg,
          'reply_markup': json.dumps(eval(str(keyboard)))
        })
  elif(text == 'dumb'):
      msg = random.choice(jokes['dumb'])
      send_message("sendMessage", {
          'chat_id': chat_id,
          'text': msg,
          'reply_markup': json.dumps(eval(str(keyboard)))
        })


@csrf_exempt
def telegram_bot(request):
  if request.method == 'POST':
    update = json.loads(request.body.decode('utf-8'))
    try: 
      update['message']
      buttons(update)
    except:
      handle_update(update)
    return HttpResponse('ok')
  else:
    return HttpResponseBadRequest('Bad Request')



