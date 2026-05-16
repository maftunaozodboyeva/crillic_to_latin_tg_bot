# import telebot
import telebot
import os
from donetv import load_dotenv
from transliterate import to_cyrillic, to_latin

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum, botimizga hush kelibsiz! Sizga qanday yordam bera olaman?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	text = message.text
	if text.isascii():
		bot.reply_to(message, to_cyrillic(text))
	else:
		bot.reply_to(message, to_latin(text))

bot.infinity_polling()

# s = input()
# if s.isascii():
#     print(to_cyrillic(s))
# else:
#     print(to_latin(s))