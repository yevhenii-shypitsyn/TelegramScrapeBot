# author Yevhenii Shypitsyn, 2020
# this is the code for Telegram bot that assists
# in scraping data from Telegram

#TeleBot API
import telebot
import config
import random

from telebot import types

#Pyrogram API
import time
import json
from pyrogram import Client
from pyrogram.errors import FloodWait

# app vars
app = Client('session', workdir='./session') 
chat = "" # name of chat
string_format = "{id},{first_name},{last_name},{username},{phone_number},{status}\n"
runResult = ""

# your TeleBot registered token
bot = telebot.TeleBot(config.TOKEN)

# /start bot
@bot.message_handler(commands=['start'])
def start(message):
    #sti = open('static/welcome.webp','rb')
    #bot.send_sticker(message.chat.id,sti)

    #markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    #item1 = types.KeyboardButton("random number")
    #item2 = types.KeyboardButton("how are things")

    #markup.add(item1,item2)

    bot.send_message(message.chat.id,"Welcome, {0.first_name}!\nYevhenii copyright 2019\nEnter name or id of chat to scrape user data\nThe chat must be public and you must have admin privilages".format(message.from_user,bot.get_me()),parse_mode='html')#, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def replyAndStartScript(message):
    if message.chat.type == 'private':
      chat = message
      scrapeData()
      bot.send_message(message.chat.id, runResult)

# further code scrapes users' info from a public group chat
# you must have admin privilages
# pyrogram API

# scraping data
def parser(id):
  members = []
  offset = 0
  limit = 200
  try:
    while True:
      chunk = app.get_chat_members(id, offset)
      
      # if no more users left
      if not chunk.chat_members:
        break
    
      members.extend(chunk.chat_members)
      offset += len(chunk.chat_members)
  except Exception as e:
    runResult = e.with_traceback
  return members

# Operations with strings
def template(data, template):
  data = json.loads(str(data))
  data['user'].setdefault('first_name', '-')
  data['user'].setdefault('last_name', '-')
  data['user'].setdefault('username', '-')
  data['user'].setdefault('phone_number', '-')
  return template.format(id=data['user']['id'],
                         first_name=data['user']['first_name'],
                         last_name=data['user']['last_name'],
                         username=data['user']['username'],
                         phone_number=data['user']['phone_number'],
                         status=data['status'])

# writing info to file
def wfile(data, template_format, path):
  with open(path, 'w', encoding='utf8') as file:
    file.writelines('# of users: {0}\n\n'.format(len(data)))
    file.writelines([template(user, template_format) for user in data])

#run scraping script when user input chat id/name
def scrapeData():
  with app:
    data = parser(chat)
    wfile(data, string_format, './chats/{0}.txt'.format(chat))
    runResult = "Success"


# run bot
bot.polling(none_stop=True)




