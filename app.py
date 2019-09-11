#!/usr/bin/python
#author @yonathansoto
#test
import os
import telebot

API_TOKEN = API_TOKEN = os.environ.get("SECRET_KEY")

bot = telebot.TeleBot(API_TOKEN)

# Con los comandos '/start' y '/help' recibiremos este mensaje
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):    
	bot.reply_to(message, "Bienvenido! Soy tu Bot")

#Esta funcion hará eco a todos tus mensajes
@bot.message_handler(func=lambda message: True)
def echo_message(message):
	bot.reply_to(message, message.text)


bot.polling()
