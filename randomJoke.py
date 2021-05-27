import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import time
import os

APITOKENJOKE = os.environ.get('APITOKENJOKE')

bot = telebot.TeleBot(APITOKENJOKE)
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup


import requests
def random_joke():
    time.sleep(0.01)
    response = requests.get(
        "https://official-joke-api.appspot.com/random_joke")
    result = response.json()
    joke =[]
    joke.append(result['type'])
    joke.append(result['setup'])
    joke.append(result['punchline'])
    return joke


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi there, I will change your unhappiness by jokes")
    msg = bot.send_message(message.chat.id, "Do you want a joke ?", reply_markup=gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    try:
        if call.data == "cb_yes":
            bot.send_message(call.from_user.id,'Type: '+random_joke()[0] +'\n'+ random_joke()[1] +'\n '+  random_joke()[2])
            time.sleep(5)
            bot.send_message(call.from_user.id, "Another one  ?", reply_markup=gen_markup())
        elif call.data == "cb_no":
            bot.send_message(call.from_user.id, "Thank you, to use it again send anything")
            
    except:
        bot.send_message(call.from_user.id, "Something went wrong ")


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Do you want a joke ?", reply_markup=gen_markup())

bot.polling()

