import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKENLR14")

bot = telebot.TeleBot(TOKEN)

reply_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
reply_kb.add("Variant А", "Variant B")

inline_kb = types.InlineKeyboardMarkup()
inline_kb.add(
    types.InlineKeyboardButton("Btn 1", callback_data="btn1"),
    types.InlineKeyboardButton("Btn 2", callback_data="btn2"),
    types.InlineKeyboardButton("Btn 3", callback_data="btn3"),
)

msg_id = None
chat_id = None

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Chose:", reply_markup=reply_kb)

@bot.message_handler(func=lambda m: m.text in ["Variant A", "Variant B"])
def handle_reply(message):
    bot.send_message(message.chat.id, f"You chose: {message.text}", reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(commands=["inline"])
def inline(message):
    global msg_id, chat_id
    msg = bot.send_message(message.chat.id, "Inline keyboard:", reply_markup=inline_kb)
    msg_id = msg.message_id
    chat_id = message.chat.id

@bot.callback_query_handler(func=lambda c: c.data in ["btn1", "btn2", "btn3"])
def callbacks(call):
    bot.answer_callback_query(call.id, f"Натиснуто {call.data}")

@bot.message_handler(commands=["delete"])
def delete(message):
    if msg_id and chat_id:
        bot.delete_message(chat_id, msg_id)

bot.polling()