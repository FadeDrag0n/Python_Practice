import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKENLR13")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.text.lower() == "привіт")
def hello(message):
    bot.reply_to(message, "Привіт")


@bot.message_handler()
def else_(message):
    bot.reply_to(message, "Я тебе не розумію")

bot.infinity_polling()