import telebot
import sqlite3

bot = telebot.TeleBot('6099814968:AAHTPHmV9Lrk01l7TbnLJ4igO9-isGt1dg8')
name = None


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('dancin.sql')
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment_primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Sup, now we will register you, enter your name')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Enter your password')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('dancin.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name , pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Users table', callback_data='users'))
    bot.send_message(message.chat.id, 'User registered', reply_markup=markup)
    # bot.send_message(message.chat.id, 'Enter your password')
    # bot.register_next_step_handler(message, user_pass)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('dancin.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Name: {el[1]}, Pass: {el[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


bot.infinity_polling()
