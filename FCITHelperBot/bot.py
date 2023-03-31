#################################################################################
#                                                                               #
#   ####    ####   ###   #####      #   #   ####   #      ####   ####    ####   #
#   #      #        #      #        #   #   #      #      #  #   #       #  #   #
#   ###    #        #      #        #####   ####   #      ####   ####    ####   #
#   #      #        #      #        #   #   #      #      #      #       # #    #
#   #       ####   ###     #        #   #   ####   ####   #      ####    #  #   #
#                                                                               #
#################################################################################



import telebot
from datetime import date
from commands_folder.updates_and_lupdates import *
from commands_folder.menu import *
from commands_folder.start import *
from commands_folder.commands import *
from commands_folder.information import *
from commands_folder.schedules_reader import *
from config import *
from telebot import types

# створюємо екземпляр бота з токеном, який отримано від BotFather
bot = telebot.TeleBot(token['TOKEN'])
#------------------------------------------------------------------------------------------------ Updates
@bot.message_handler(commands=['updates'])
def updates(updates):
    user_name = updates.from_user.first_name
    print(f"{user_name} викликав команду /updates")
    updates_info(updates, bot)
#------------------------------------------------------------------------------------------------ Information
@bot.message_handler(commands = ['info'])
def info(info):
    user_name = info.from_user.first_name
    print(f"{user_name} викликав команду /info")
    information(info, bot)
#------------------------------------------------------------------------------------------------ Last Update
@bot.message_handler(commands=['lupdates'])
def lupdates(lupdates):
    user_name = lupdates.from_user.first_name
    print(f"{user_name} викликав команду /lupdates")
    lupdates_info(lupdates, bot)
#------------------------------------------------------------------------------------------------ Menu
@bot.message_handler(commands = ['menu'])
def commands(menu):
    user_name = menu.from_user.first_name
    print(f"{user_name} викликав команду /menu")
    menu_handler(menu, bot)
#------------------------------------------------------------------------------------------------ Schedules
@bot.message_handler(commands=['schedules', 'schedule', 'sched', 'sc'])
def test_buttons(message):
    markup = types.InlineKeyboardMarkup()
    schedules = [
        {"text": "КНШІ-11", "callback": "knai_11_today"},
        {"text": "КН-11", "callback": "kn_11_today"},
        {"text": "КН-12", "callback": "kn_12_today"}
    ]
    for s in schedules:
        button = types.InlineKeyboardButton(text=s["text"], callback_data=s["callback"])
        markup.add(button)

    bot.send_message(message.chat.id, "Виберіть ваш розклад:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    schedules = {
        "knai_11_today": knai_11,
        "kn_11_today": kn_11,
        "kn_12_today": kn_12,
    }
    get_day_of_week(date.today().strftime("%d.%m"), call.message, bot, schedules[call.data])
#------------------------------------------------------------------------------------------------ Commands
@bot.message_handler(commands=['commands'])
def commands(commands):
    user_name = commands.from_user.first_name
    print(f"{user_name} викликав команду /commands")
    commands_info(commands, bot)
#------------------------------------------------------------------------------------------------ Start
@bot.message_handler(commands=['start'])
def start(start):
    user_name = start.from_user.first_name
    print(f"{user_name} викликав команду /start")
    hello_start(start, bot)

#===================================#
# запускаємо бота                   #
print("Bot was started")            #
bot.polling()                       #
#===================================#