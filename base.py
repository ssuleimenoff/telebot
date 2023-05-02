import telebot
import webbrowser

bot = telebot.TeleBot('6099814968:AAHTPHmV9Lrk01l7TbnLJ4igO9-isGt1dg8')


@bot.message_handler(commands=['site', 'website', 'github'])
def site(message):
    webbrowser.open('https://github.com/ssuleimenoff/pp2-22B030590')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     f'Hello {message.from_user.first_name} {message.from_user.last_name}, I am a newly created bot from @ssuleimenovv')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


@bot.message_handler(commands=['message'])
def main(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id,
                         f'Hello {message.from_user.first_name} {message.from_user.last_name}, I am a newly created bot from @ssuleimenovv')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.infinity_polling()
