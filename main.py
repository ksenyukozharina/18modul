import telebot


bot = telebot.TeleBot('6333341029:AAEYh48o-LdR4sUHbI__dUDjQDucCQG1KJQ')

@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f'Приветсвую, {message.chat.active_username}')

bot.polling(none_stop=True)