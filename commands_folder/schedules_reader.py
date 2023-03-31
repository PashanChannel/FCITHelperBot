import datetime
from schedules import *
def is_week_even(date_string):
    date = datetime.datetime.strptime(date_string, '%d.%m.%Y')
    week_number = date.isocalendar()[1]
    if week_number % 2 == 0:
        return 2
    else:
        return 1
def get_day_of_week(date, message, bot, schedule):
    try:
        date_obj = datetime.datetime.strptime(f"{date}.2023", '%d.%m.%Y')
        day_of_week = date_obj.strftime('%A')
        if is_week_even(f"{date}.2023") == 2:
            bot.reply_to(message, "Сьогодні вихідний, можеш балдіти :)" if day_of_week in ('Saturday', 'Sunday') else schedule[day_of_week]["pair"])
        else:
            bot.reply_to(message, "Сьогодні вихідний, можеш балдіти :)" if day_of_week in ('Saturday', 'Sunday') else schedule[day_of_week]["not_even"])
    except ValueError:
        bot.reply_to(message, "Неправильний формат дати! Введіть дату у форматі 'дд.мм'")