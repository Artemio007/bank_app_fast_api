import logging

import telebot
from telebot import types
from datetime import datetime
from random import randint

from app.apis_all_banks.nb_rb_api.nb_rb_redis import nb_rb_get_from_redis
from app.core.config import settings
from app.currensy_calc.calc_nb import calc

bot = telebot.TeleBot(settings.TOKEN_BOT, parse_mode=None)
start_count = 0
value = ""
res_value = ""


@bot.message_handler(commands=['start'])
def get_curr(message):
    global start_count
    print(start_count)
    if not start_count:
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_cur = types.KeyboardButton(text="Дай курс валют на сегодня")
        button_cur_2 = types.KeyboardButton(text="Валютный калькулятор")
        keyboard.add(button_cur, button_cur_2)
        bot.send_message(message.chat.id, f"Привет {message.chat.first_name}", reply_markup=keyboard)
        start_count += 1
    elif start_count in range(1, 3):
        bot.send_message(message.chat.id, f"{message.chat.first_name}, мы уже здоровались.")
        start_count += 1
    elif start_count in range(3, 5):
        bot.send_message(message.chat.id, f"{message.chat.first_name}, перестань пожалуйста.")
        start_count += 1
    else:
        bot.send_message(message.chat.id, f"{message.chat.first_name}, если хочешь начать заново введи: /repeat")


@bot.message_handler(func=lambda message: message.text == 'Дай курс валют на сегодня')
def send_nb_rb(message):
    result = nb_rb_get_from_redis()
    info = result.replace("  ", "\n")
    mess = f"Курс валют по нацбанку РБ ({datetime.now()})\n{info}"
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['repeat'])
def rep(message):
    global start_count
    start_count = 0
    get_curr(message)


@bot.message_handler(func=lambda message: message.text == 'Валютный калькулятор')
def currency_calc(message):
    global keyboard_

    keyboard_ = telebot.types.InlineKeyboardMarkup()
    keyboard_.row(
        telebot.types.InlineKeyboardButton("C", callback_data="C"),
        telebot.types.InlineKeyboardButton("<=", callback_data="<="),

    )
    keyboard_.row(
        telebot.types.InlineKeyboardButton("7", callback_data="7"),
        telebot.types.InlineKeyboardButton("8", callback_data="8"),
        telebot.types.InlineKeyboardButton("9", callback_data="9"),

    )
    keyboard_.row(
        telebot.types.InlineKeyboardButton("4", callback_data="4"),
        telebot.types.InlineKeyboardButton("5", callback_data="5"),
        telebot.types.InlineKeyboardButton("6", callback_data="6"),
    )
    keyboard_.row(
        telebot.types.InlineKeyboardButton("1", callback_data="1"),
        telebot.types.InlineKeyboardButton("2", callback_data="2"),
        telebot.types.InlineKeyboardButton("3", callback_data="3"),

    )
    keyboard_.row(
        telebot.types.InlineKeyboardButton("0", callback_data="0"),
        telebot.types.InlineKeyboardButton(".", callback_data="."),
        telebot.types.InlineKeyboardButton("=", callback_data="=")
    )
    keyboard_.row(
        telebot.types.InlineKeyboardButton("BYN", callback_data="BYN"),
        telebot.types.InlineKeyboardButton("USD", callback_data="USD"),
        telebot.types.InlineKeyboardButton("EUR", callback_data="EUR")
    )
    keyboard_.row(
        telebot.types.InlineKeyboardButton("RUB", callback_data="RUB"),
        telebot.types.InlineKeyboardButton("CNY", callback_data="CNY"),
        telebot.types.InlineKeyboardButton("AED", callback_data="AED")
    )
    keyboard_.row(
        telebot.types.InlineKeyboardButton("Инструкция", callback_data="Инструкция"),
        telebot.types.InlineKeyboardButton("Перевести в", callback_data=" -> "),
    )

    bot.send_message(message.chat.id, "0", reply_markup=keyboard_)


@bot.callback_query_handler(func=lambda call: True)
def callback_foo(query):
    global value, res_value
    data = query.data
    if data == "C":
        value = ""
    elif data == "<=":
        value = value[0:-1]

    elif data == "=":
        try:
            res = value.split()
            value = str(calc(res[3], res[1], float(res[0]))) + f" {res[3]}"
        except Exception as err:
            logging.info(err)
            value = "Ошибка"
    elif data.isdigit() or data == ".":
        value += data
    elif data == "BYN":
        value += " BYN "
    elif data == "USD":
        value += " USD "
    elif data == "EUR":
        value += " EUR "
    elif data == "RUB":
        value += " RUB "
    elif data == "CNY":
        value += " CNY "
    elif data == "AED":
        value += " AED "
    elif data == " -> ":
        value += " -> "
    elif data == "Инструкция":
        with open(r"D:\BankAggregator\bank_api\backend\app\currency_bot\txtmess\instruct.txt", "r", encoding="utf-8") as answ:
            answer = answ.read()
            bot.send_message(chat_id=query.message.chat.id, text=answer)

    if value != res_value:
        if value == "":
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text="0",
                                  reply_markup=keyboard_)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text=value,
                                  reply_markup=keyboard_)
        res_value = value


@bot.message_handler()
def send_text(message):
    with open(r"D:\BankAggregator\bank_api\backend\app\currency_bot\txtmess\phrases.txt", "r", encoding="utf-8") as answ:
        answer = answ.readlines()
    bot.send_message(message.chat.id, answer[randint(0, 10)])


