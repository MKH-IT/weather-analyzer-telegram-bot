import time

import schedule
import telebot
from decouple import config
from telebot import types

from database import JSONDatabase
from helpers import get_weather_by_location
from models import UserRepositoryJSONHandler, User

TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN")

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)
database = UserRepositoryJSONHandler(database=JSONDatabase())
temp_database = {}


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
    user = User(user_id=message.chat.id)
    database.create_user(user)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text in ["English 🇬🇧", "Русский язык 🇷🇺"]:
        print(message.text)  # TODO: Save the language to the database.
        bot.send_message(message.chat.id, f"You selected {message.text}.")
        ask_location(message)
    elif message.text in ["06:00", "07:00", "08:00", "09:00"]:
        print(message.text)  # TODO: Save the selected option to the database.
        remove_keyboard = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(
            message.chat.id,
            f"You selected option {message.text}",
            reply_markup=remove_keyboard,
        )
    else:
        bot.send_message(message.chat.id, "This text cannot be processed.")


def ask_location(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(types.KeyboardButton("Share Location", request_location=True))
    bot.send_message(
        message.chat.id, "Please share your location:", reply_markup=markup
    )


@bot.message_handler(content_types=["location"])
def handle_location(message):
    print(message)  # TODO: Save the location to the database.
    temp_database[message.chat.id] = {  # TODO: temp solution.
        "latitude": float(message.location.latitude),
        "longitude": float(message.location.longitude),
    }
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
    ask_notification_time(message)


def ask_notification_time(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(
        types.KeyboardButton("06:00"),
        types.KeyboardButton("07:00"),
        types.KeyboardButton("08:00"),
        types.KeyboardButton("09:00"),
    )
    bot.send_message(
        message.chat.id,
        """
        🌞 Please select a time to receive notifications:
        """,
        reply_markup=markup,
    )
    send_weather_info(
        message.chat.id, **temp_database[message.chat.id]
    )  # TODO: temp solution.


def send_weather_info(chat_id: str, latitude: float, longitude: float):
    weather_info = get_weather_by_location(
        latitude=latitude,
        longitude=longitude,
    )
    bot.send_message(chat_id, f"Current weather info {weather_info}")


def send_weather_info_bulk():
    """
    Function to send weather information to all users on the specified time.
    """
    for chat_id, location in temp_database.items():
        send_weather_info(chat_id, *location.values())


def main():
    bot.polling(non_stop=True)
    schedule.every().hour.do(send_weather_info)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
