import telebot
from telebot import types

bot = telebot.TeleBot('6099814968:AAHTPHmV9Lrk01l7TbnLJ4igO9-isGt1dg8')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на github')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    file = open('./aaron-smith-dancin-speed-up-mp3.mp3', 'rb')
    bot.send_audio(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Hello', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на github', url='https://github.com/ssuleimenoff/pp2-22B030590')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)

    bot.reply_to(message, 'xD', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


bot.infinity_polling()
