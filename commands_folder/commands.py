def commands_info(commands, bot):
   bot.reply_to(commands, "/start - Запуск бота\n"
                "/commands - Доступні команди.\n"
                "/info - Інформація.\n"
                "/schedules або /sc - глянути доступний розклад\n"
                "/bugreport - відправлення звіту про помилку або баг\n"
                "/updates - Список обновлень\n"
                "/lupdates - Останні обновлення\n")
