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
from telebot.types import Message
from datetime import date
import logging
from for_owner.save_group_id import *
from commands_folder.updates_and_lupdates import *
from commands_folder.menu import *
from commands_folder.start import *
from commands_folder.commands import *
from commands_folder.information import *
from commands_folder.schedules_reader import *
from config import *
import json
from telebot import types

def delete_user_message(update, context):
    message_id = update.message.message_id  # отримуємо ID повідомлення
    chat_id = update.message.chat_id  # отримуємо ID чату
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)

commands_logger = logging.getLogger('commands')
commands_logger.setLevel(logging.INFO)
comm = logging.FileHandler('myapp.log')
comm.setLevel(logging.INFO)
formula = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
comm.setFormatter(formula)
commands_logger.addHandler(comm)

chat_logger = logging.getLogger('chat')
chat_logger.setLevel(logging.INFO)

# Встановити обробник, який буде записувати логи у файл chat.log
handler = logging.FileHandler('chat.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
chat_logger.addHandler(handler)

bot = telebot.TeleBot(token['TOKEN'])
###############################TEST ZONE#######################################

###############################TEST ZONE#######################################

#------------------------------------------------------------------------------------------------ Bug Report
@bot.message_handler(commands=['bugreport'])
def bugreport(message):
    if len(message.text.split(maxsplit=1)) > 1:
        report_message = message.text.split(maxsplit=1)[1]
        bot.send_message(chat_id='-1001892413516', text=f'Нова скарга від користувача \@{message.from_user.username}:\nСуть скарги: {report_message}')
    else:
        bot.send_message(chat_id=message.chat.id, text="Будь ласка, введіть опис проблеми в форматі /bugreport ваша скарга")
#------------------------------------------------------------------------------------------------ Updates-1001892413516
@bot.message_handler(commands=['updates'])
def updates(updates):
    user_name = updates.from_user.username
    commands_logger.info(f"{user_name} called command /updates")
    
    updates_info(updates, bot)
#------------------------------------------------------------------------------------------------ Information
@bot.message_handler(commands = ['info'])
def info(info):
    user_name = info.from_user.username
    commands_logger.info(f"{user_name} called command /info")
    information(info, bot)
#------------------------------------------------------------------------------------------------ Last Update
@bot.message_handler(commands=['lupdates'])
def lupdates(lupdates):
    user_name = lupdates.from_user.username
    commands_logger.info(f"{user_name} called command /lupdates")
    lupdates_info(lupdates, bot)
#------------------------------------------------------------------------------------------------ Menu
@bot.message_handler(commands = ['menu'])
def commands(menu):
    user_name = menu.from_user.username
    commands_logger.info(f"{user_name} called command /menu")
    menu_handler(menu, bot)
#------------------------------------------------------------------------------------------------ Schedules
@bot.message_handler(commands=['schedules', 'sc'])
def test_buttons(message):
    user_name = message.from_user.username
    logging.info(f"{user_name} called command /schedules")
    markup = types.InlineKeyboardMarkup()
    schedules = [
        {"text": "СА-11", "callback": "СА-11_today"},
        {"text": "ІСТ-11", "callback": "ІСТ-11_today"},
        {"text": "ІПЗ-11", "callback": "ІПЗ-11_today"},
        {"text": "ІПЗ-12", "callback": "ІПЗ-12_today"},
        {"text": "КІ-11", "callback": "КІ-11_today"},
        {"text": "МТІР-11", "callback": "МТІР-11_today"},
        {"text": "АКІТ-11", "callback": "АКІТ-11_today"},
        {"text": "АКІТ-12", "callback": "АКІТ-12_today"},
        {"text": "КБ-11", "callback": "КБ-11_today"},
        {"text": "КБ-12", "callback": "КБ-12_today"},
        {"text": "КН-11", "callback": "КН-11_today"},
        {"text": "КН-12", "callback": "КН-12_today"},
        {"text": "КНШІ-11", "callback": "КНШІ-11_today"},
        {"text": "ЕК-11", "callback": "ЕК-11_today"},
        {"text": "ЦТ-11", "callback": "ЦТ-11_today"},
        {"text": "ЦТ-12", "callback": "ЦТ-12_today"}
    ]
    row = []  # список кнопок, що будуть в одному ряді
    for i, s in enumerate(schedules):
        button = types.InlineKeyboardButton(text=s["text"], callback_data=s["callback"])
        row.append(button)
        if i % 4 == 3:  # якщо кнопок у ряді вже 4
            markup.row(*row)  # додати ці кнопки до розмітки
            row = []  # почати новий ряд кнопок
    if row:  # якщо залишилися кнопки в останньому ряду
        markup.row(*row)  # додати їх до розмітки
    close_button = types.InlineKeyboardButton(text="<< Закрити >>", callback_data="close")
    markup.add(close_button)
    bot.reply_to(message, "Виберіть ваш розклад:", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "close":
        # якщо користувач натиснув кнопку "Закрити", видаляємо повідомлення
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    else:
        schedules = {
            "СА-11_today": ca_11,
            "ІСТ-11_today": ict_11,
            "ІПЗ-11_today": ipz_11,
            "ІПЗ-12_today": ipz_12,
            "КІ-11_today": ki_11,
            "МТІР-11_today" : mtir_11,
            "АКІТ-11_today": akit_11,
            "АКІТ-12_today": akit_12,
            "КБ-11_today": kb_11,
            "КБ-12_today": kb_12, #Processing
            "КН-11_today": kn_11,
            "КН-12_today": kn_12,
            "КНШІ-11_today": knai_11,
            "ЕК-11_today": ek_11, #Processing
            "ЦТ-11_today": tst_11, #Processing
            "ЦТ-12_today": tst_12, #Processing
        }
        button_text = call.data  # отримуємо текст кнопки, яку натиснув користувач
        user_name = call.from_user.username
        logging.info(f"{user_name} pressed button: {button_text}")
        group_name = button_text.replace("_today", "").upper()
        get_day_of_week(date.today().strftime("%d.%m"), call.message, bot, schedules[call.data], group_name)
#------------------------------------------------------------------------------------------------ Commands
@bot.message_handler(commands=['commands'])
def commands(commands):
    user_name = commands.from_user.username
    commands_logger.info(f"{user_name} called command /commands")
    commands_info(commands, bot)
#------------------------------------------------------------------------------------------------ Start
@bot.message_handler(commands=['start'])
def start(start):
    user_name = start.from_user.username
    commands_logger.info(f"{user_name} called command /start")
    hello_start(start, bot)
#------------------------------------------------------------------------------------------------ Spy
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_type = message.chat.type
    chat_logger.info(f'{chat_type}: {message.chat.username}: {message.text}')
#=======================================#
# запускаємо бота                       #
commands_logger.info("Bot was started") #
chat_logger.info("Bot was started")     #
print("Bot was started")                #
bot.polling(none_stop=True)             #
#=======================================#
