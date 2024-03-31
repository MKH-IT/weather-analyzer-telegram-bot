import telebot
from decouple import config
from telebot import types

from database import JSONDatabase, Database
from helpers import gen_languages_markup

TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN")

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Hello! {message.from_user.first_name}!",
        reply_markup=gen_languages_markup(),
    )
    bot.register_next_step_handler(message, on_click_language)


@bot.callback_query_handler(func=lambda call: call.data.startswith("language_"))
def on_click_language(call):
    if call.data == "language_english":
        bot.answer_callback_query(call.id, "You selected English language.")
    elif call.data == "language_russian":
        bot.answer_callback_query(call.id, "You selected Russian language.")
    elif call.data == "language_uzbek":
        bot.answer_callback_query(call.id, "You selected Uzbek language.")
    ask_for_location(call.message.chat.id)


def ask_for_location(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    location_button = types.KeyboardButton(text="Send Location", request_location=True)
    markup.add(location_button)
    bot.send_message(chat_id, "Please share your location:", reply_markup=markup)
    bot.register_next_step_handler_by_chat_id(chat_id, process_location)


def process_location(message):
    location = message.location
    print(location)
    # Do something with the location data
    ask_for_phone_number(message.chat.id)


def ask_for_phone_number(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    phone_number_button = types.KeyboardButton(
        text="Send phone number", request_contact=True
    )
    markup.add(phone_number_button)
    bot.send_message(chat_id, "Please share your phone number:", reply_markup=markup)
    bot.register_next_step_handler_by_chat_id(chat_id, process_phone_number)


def process_phone_number(message):
    phone_number = message.text
    print(phone_number)
    # Do something with the phone number
    bot.send_message(message.chat.id, "Thank you for sharing your information!")


def main():
    database = Database(JSONDatabase())
    bot.polling(non_stop=True)


if __name__ == "__main__":
    main()
