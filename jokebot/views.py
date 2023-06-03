from django.shortcuts import render
import json
import requests
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from jokebot.cred import TELEGRAM_API_URL
from jokebot.models import *
from telegram.ext import *
from telegram import *
from jokebot.logic import *

def index(request):
    obj = noOfCalls.objects.all()
    context ={
        "obj":obj,
        }
    return render(request, "index.html",context)

def send_message(method, data):
  return requests.post(TELEGRAM_API_URL + method, data)


@csrf_exempt
def telegram_bot(request):
  if request.method == 'POST':
    update = json.loads(request.body.decode('utf-8'))
    try:
      update['message']
      values = buttons(update)
      send_message(values[0],values[1])
    except:
      chat_id = update['callback_query']['from']['id']
      text = update['callback_query']['data'].lower()
      db_id = noOfCalls.objects.filter(user_id = chat_id)
      d = s = f = 0
      if(text == 'stupid'):
         s = 1
      elif(text == 'fat'):
         f = 1
      elif(text == 'dumb'):
        d = 1
      if db_id.exists():
         cur_val = noOfCalls.objects.get(user_id = chat_id)
         if(text == 'stupid'):
            cur_val.stupid = cur_val.stupid + 1
         elif(text == 'fat'):
            cur_val.fat = cur_val.fat + 1
         elif(text == 'dumb'):
           cur_val.dumb = cur_val.dumb + 1
         cur_val.save()
      else:
        db_update = noOfCalls(user_id = chat_id, stupid=s, fat=f, dumb=d)
        db_update.save()
      values = handle_update(update)
      send_message(values[0],values[1])
    return HttpResponse('ok')
  else:
    return HttpResponseBadRequest('Bad Request')



