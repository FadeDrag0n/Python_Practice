import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKENLR13")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f"Hello {message.from_user.first_name}!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()