import telebot
#import openai
import datetime
from config import *
from commands import *
# створюємо екземпляр бота з токеном, який отримано від BotFather
bot = telebot.TeleBot(token['TOKEN'])
#openai.api_key = "SECRET"
#gpt_model = "code-davinci-002"

#def generate_response(prompt):
#    response = openai.Completion.create(
#        engine=gpt_model,
#        prompt=prompt,
#        max_tokens=100,
#        n=1,
#        stop=None,
#        temperature = 0.7,
#    )
#    return response.choices[0].text.strip()

#@bot.message_handler(commands=['gpt'])
#def generate_and_reply(message):
#    if message.text:
#        prompt = message.text.replace('/gpt', '').strip()
#        response = generate_response(prompt)
#        bot.reply_to(message, response)


#Перевіряємо чи парний тиждень
@bot.message_handler(commands=['updates'])
def updates(updates):
    updates_info(updates, bot)
@bot.message_handler(commands=['lupdates'])
def lupdates(lupdates):
    lupdates_info(lupdates, bot)
@bot.message_handler(commands=['knai_11'])
def knAi_11(message):
    try:
        date = message.text.split(" ")
        get_day_of_week_for_knai_11(date[1], message, bot)
    except:
        today = datetime.datetime.today()
        get_day_of_week_for_knai_11(today.strftime("%d.%m"), message, bot)
@bot.message_handler(commands=['kn_11'])
def Kn_11(message):
    try:
        date = message.text.split(" ")
        get_day_of_week_for_kn_11(date[1], message, bot)
    except:
        today = datetime.datetime.today()
        get_day_of_week_for_kn_11(today.strftime("%d.%m"), message, bot)
@bot.message_handler(commands=['kn_12'])
def Kn_12(message):
    try:
        date = message.text.split(" ")
        get_day_of_week_for_kn_12(date[1], message, bot)
    except:
        today = datetime.datetime.today()
        get_day_of_week_for_kn_12(today.strftime("%d.%m"), message, bot)
@bot.message_handler(commands=['commands'])
def commands(commands):
    commands_info(commands, bot)
@bot.message_handler(commands=['start'])
def start(start):
    hello_start(start, bot)

# запускаємо бота
print("Bot was started")
bot.polling()