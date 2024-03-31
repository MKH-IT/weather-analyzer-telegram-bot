from datetime import datetime

import telebot
from decouple import config
from telebot import types
import schedule
import time

from database import JSONDatabase
from models import UserRepositoryJSONHandler

TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN")

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(
        types.KeyboardButton("English 🇬🇧"), types.KeyboardButton("Русский язык 🇷🇺")
    )
    bot.send_message(
        message.chat.id,
        """
        🇬🇧 Please select a language: \n🇷🇺 Пожалуйста, выберите язык:
        """,
        reply_markup=markup,
    )


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "English 🇬🇧":
        ask_location(message)
    elif message.text == "Русский язык 🇷🇺":
        ask_location(message)
    else:
        bot.send_message(message.chat.id, "Please select a valid language.")

    print(message.text)  # TODO: Save the language to the database.


def ask_location(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(types.KeyboardButton("Share Location", request_location=True))
    bot.send_message(
        message.chat.id, "Please share your location:", reply_markup=markup
    )


@bot.message_handler(content_types=["location"])
def handle_location(message):
    print(message)  # TODO: Save the location to the database.
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
def handle_phone_number(message):
    print(message)  # TODO: Save the phone number to the database.
    remove_keyboard = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(
        message.chat.id,
        "Thank you! Your phone number has been recorded.",
        reply_markup=remove_keyboard,
    )


def send_weather_info():
    """
    Function to send weather information to all users on the specified time.
    """
    chat_ids = []  # TODO: Get chat_ids from the database.
    message = f"This is a scheduled message. {datetime.now()}"
    for chat_id in chat_ids:
        bot.send_message(chat_id=chat_id, text=message)


def main():
    database = UserRepositoryJSONHandler(database=JSONDatabase())
    bot.polling(non_stop=True)
    schedule.every().hour.do(send_weather_info)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
