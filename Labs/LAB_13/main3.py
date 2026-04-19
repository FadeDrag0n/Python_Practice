import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKENLR13")

bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['register'])
def start(message):
    bot.send_message(message.chat.id, "Введіть ваше ім'я:")
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    name = message.text

    bot.send_message(message.chat.id, "Введіть ваше прізвище:")
    bot.register_next_step_handler(message, get_age, name)

def get_age(message, name):
    surname = message.text

    bot.send_message(message.chat.id, "Введіть ваш вік:")
    bot.register_next_step_handler(message, finish, name, surname)

def finish(message, name, surname):
    age = message.text

    bot.send_message(
        message.chat.id,
        f"Дякую! Ось ваші дані:\n"
        f"Ім'я: {name}\n"
        f"Прізвище: {surname}\n"
        f"Вік: {age}"
    )



@bot.message_handler()
def else_(message):
    bot.reply_to(message, "Введіть /register")

bot.infinity_polling()