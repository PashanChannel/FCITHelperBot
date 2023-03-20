import telebot
import datetime
from config import token
from schedules import knai_11, kn_11, kn_12

# створюємо екземпляр бота з токеном, який отримано від BotFather
bot = telebot.TeleBot(token['TOKEN'])
#Перевіряємо чи парний тиждень
def is_week_even(date_string):
    date = datetime.datetime.strptime(date_string, '%d.%m.%Y')
    week_number = date.isocalendar()[1]
    if week_number % 2 == 0:
        return 2
    else:
        return 1


def get_day_of_week_for_knai_11(date, message):
    try:
        # конвертуємо текст повідомлення в об'єкт дати
        date_obj = datetime.datetime.strptime(f"{date}.2023", '%d.%m.%Y')
        # отримуємо день тижня з об'єкту дати та відправляємо його користувачу
        day_of_week = date_obj.strftime('%A')
        if is_week_even(f"{date}.2023") == 2:
            if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                bot.reply_to(message, "Сьогодні вихідний, можеш балдіти :)")
                return
            else:
                bot.reply_to(message, knai_11[day_of_week]["pair"])
        else:
            if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                bot.reply_to(message, "Сьогодні вихідний, можеш балдіти :)")
                return
            bot.reply_to(message, knai_11[day_of_week]["not_even"])
    except ValueError:
        bot.reply_to(message, "Неправильний формат дати! Введіть дату у форматі 'дд.мм'")
def get_day_of_week_for_kn_11(date, message):
    try:
        # конвертуємо текст повідомлення в об'єкт дати
        date_obj = datetime.datetime.strptime(f"{date}.2023", '%d.%m.%Y')
        # отримуємо день тижня з об'єкту дати та відправляємо його користувачу
        day_of_week = date_obj.strftime('%A')
        if is_week_even(f"{date}.2023") == 2:
            if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                bot.reply_to(message, "Сьогодні вихідний, можеш балдіти :)")
                return
            else:
                bot.reply_to(message, kn_11[day_of_week]["pair"])
        else:
            if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                bot.reply_to(message, "Сьогодні вихідний, можеш балдіти :)")
                return
            bot.reply_to(message, kn_11[day_of_week]["not_even"])
    except ValueError:
        bot.reply_to(message, "Неправильний формат дати! Введіть дату у форматі 'дд.мм'")
def get_day_of_week_for_kn_12(date, message):
    try:
        # конвертуємо текст повідомлення в об'єкт дати
        date_obj = datetime.datetime.strptime(f"{date}.2023", '%d.%m.%Y')
        # отримуємо день тижня з об'єкту дати та відправляємо його користувачу
        day_of_week = date_obj.strftime('%A')
        if is_week_even(f"{date}.2023") == 2:
            if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                bot.reply_to(message, "Сьогодні вихідний, можеш балдіти :)")
                return
            else:
                bot.reply_to(message, kn_12[day_of_week]["pair"])
        else:
            if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                bot.reply_to(message, "Сьогодні вихідний, можеш балдіти :)")
                return
            bot.reply_to(message, kn_12[day_of_week]["not_even"])
    except ValueError:
        bot.reply_to(message, "Неправильний формат дати! Введіть дату у форматі 'дд.мм'")
def lupdates_info(lupdates):
    bot.reply_to(lupdates, "Обновлення 17.03\n- Доданий розклад для КНШІ-11, КН-11, КН-12\n- Додані команди /knai_11 | /kn_11 | /kn_12\n- Додана команда /commands де описують дію функції")
def updates_info(updates):
    bot.reply_to(updates, "Обновлення 16.03\n- Доданий розклад для КНШІ-11 та частково КН-11\n- Додані команди /kndai_11 та /kn_11")
@bot.message_handler(commands=['updates'])
def updates(updates):
    updates_info(updates)
@bot.message_handler(commands=['lupdates'])
def lupdates(lupdates):
    lupdates_info(lupdates)
@bot.message_handler(commands=['knai_11'])
def knAi_11(message):
    try:
        date = message.text.split(" ")
        get_day_of_week_for_knai_11(date[1], message)
    except:
        today = datetime.datetime.today()
        get_day_of_week_for_knai_11(today.strftime("%d.%m"), message)
@bot.message_handler(commands=['kn_11'])
def Kn_11(message):
    try:
        date = message.text.split(" ")
        get_day_of_week_for_kn_11(date[1], message)
    except:
        today = datetime.datetime.today()
        get_day_of_week_for_kn_11(today.strftime("%d.%m"), message)
@bot.message_handler(commands=['kn_12'])
def Kn_12(message):
    try:
        date = message.text.split(" ")
        get_day_of_week_for_kn_12(date[1], message)
    except:
        today = datetime.datetime.today()
        get_day_of_week_for_kn_12(today.strftime("%d.%m"), message)
@bot.message_handler(commands=['commands'])
def commands(commands):
    commands_info(commands)

def commands_info(commands):
    bot.reply_to(commands, "/kn_11, /kn_12, /knai_11 - Розклад для певної групи.\nНаприклад: /knai_11 - видає розклад на поточний день. А якщо написати /knai_11 17.03, то видасть розклад на задану дату.\n/lupdates - видає останнє обновлення бота")

@bot.message_handler(commands=['start'])
def start(start):
    hello_start(start)

def hello_start(start):
    bot.reply_to(start, "Привіт! Я - ФКІТ помічник Адольф :)\nЯ вмію показувати розклад групам які є в моїй базі.\nПропоную тобі написати /commands щоб дізнатися мій функціонал)")
# запускаємо бота
print("Bot was started")
bot.polling()