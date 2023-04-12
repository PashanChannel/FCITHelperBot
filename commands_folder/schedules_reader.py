import datetime
from telebot import types
from schedules import *
def get_next_day_button(call, bot, group_name, schedule):
    date_obj = datetime.datetime.strptime(call.data, "%d.%m.%Y")
    next_day = date_obj + datetime.timedelta(days=1)
    next_day_str = next_day.strftime("%d.%m.%Y")
    get_day_of_week(next_day_str, call.message, bot, schedule, group_name)

def is_week_even(date_string):
    date = datetime.datetime.strptime(date_string, '%d.%m.%Y')
    week_number = date.isocalendar()[1]
    if week_number % 2 == 0:
        return 2
    else:
        return 1

def get_day_of_week(date, message, bot, schedule, group_name):
    def delete_message():
        try:
            bot.delete_message(chat_id=text.chat.id, message_id=text.message_id)
        except Exception as e:
            print(e)
    try:
        date_obj = datetime.datetime.strptime(f"{date}.2023", '%d.%m.%Y')
        day_of_week = date_obj.strftime('%A')
        month_dict = {
            1: "Січень", 2: "Лютий",
            3: "Березень", 4: "Квітень",
            5: "Травень", 6: "Червень",
            7: "Липень", 8: "Серпень",
            9: "Вересень", 10: "Жовтень",
            11: "Листопад", 12: "Грудень"
        }
        month_num = int(date_obj.strftime('%m'))
        month_name = month_dict[month_num]
        day_num = date_obj.strftime('%d')
        if is_week_even(f"{date}.2023") == 2:
            if day_of_week in ('Saturday', 'Sunday'):
                bot.reply_to(message, "Сьогодні вихідний, можеш балдіти :)")
                markup = types.InlineKeyboardMarkup()
                close_button = types.InlineKeyboardButton("Закрити", callback_data="close")
                markup.add(close_button)
                bot.reply_to(message, text, reply_markup=markup)
            else:
                text = f"{group_name} {month_name} {day_num} \nПарний тиждень\n\n{schedule[day_of_week]['pair']}"
                markup = types.InlineKeyboardMarkup()
                close_button = types.InlineKeyboardButton("Закрити", callback_data="close")
                markup = get_next_day_button(date_obj, bot, group_name, schedule)
                markup.add(close_button)
                bot.reply_to(message, text, reply_markup=markup)
        else:
            if day_of_week in ('Saturday', 'Sunday'):
                bot.reply_to(message, "Сьогодні вихідний, можеш балдіти :)")
            else:
                text = f"{group_name} {month_name} {day_num} \nНепарний тиждень \n\n{schedule[day_of_week]['not_even']}"
                markup = types.InlineKeyboardMarkup()
                close_button = types.InlineKeyboardButton("Закрити", callback_data="close")
                markup = get_next_day_button(date_obj, bot, group_name, schedule)
                markup.add(close_button)
                bot.reply_to(message, text, reply_markup=markup)
    except ValueError:  
        bot.reply_to(message, "Неправильний формат дати! Введіть дату у форматі 'дд.мм'")
        markup = types.InlineKeyboardMarkup()
        close_button = types.InlineKeyboardButton("Закрити", callback_data="close")
        markup.add(close_button)
        bot.reply_to(message, text, reply_markup=markup)