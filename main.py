import telebot
from decouple import config
from telebot import types

from database import JSONDatabase
from models import UserRepositoryJSONHandler

TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN")

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(types.KeyboardButton("English 🇬🇧"), types.KeyboardButton("Russian 🇷🇺"))
    bot.send_message(
        message.chat.id,
        "Please select a language:",
        reply_markup=markup,
    )


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "English 🇬🇧":
        ask_location(message)
    elif message.text == "Russian 🇷🇺":
        ask_location(message)
    else:
        bot.send_message(message.chat.id, "Please select a valid language.")


def ask_location(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(types.KeyboardButton("Share Location", request_location=True))
    bot.send_message(
        message.chat.id, "Please share your location:", reply_markup=markup
    )


@bot.message_handler(content_types=["location"])
def handle_location(message):
    print(message)
    ask_phone_number(message)


def ask_phone_number(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    phone_number_button = types.KeyboardButton(
        text="Send phone number", request_contact=True
    )
    markup.add(phone_number_button)
    bot.send_message(
        message.chat.id, "Please send your phone number:", reply_markup=markup
    )


@bot.message_handler(content_types=["contact"])
def handle_contact(message):
    print(message)
    remove_keyboard = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(
        message.chat.id,
        "Thank you! Your phone number has been recorded.",
        reply_markup=remove_keyboard,
    )


def main():
    database = UserRepositoryJSONHandler(database=JSONDatabase())
    bot.polling(non_stop=True)


if __name__ == "__main__":
    main()
