import telebot
from telebot import types
from decouple import config

from database import DatabaseBase, JSONDatabase, Database

TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN")

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    languages = [
        types.KeyboardButton("English"),
        types.KeyboardButton("Russian"),
        types.KeyboardButton("Uzbek"),
    ]
    markup.add(*languages)
    bot.send_message(
        message.chat.id, f"Hello! {message.from_user.first_name}", reply_markup=markup
    )
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == "English":
        bot.send_message(message.chat.id, "You selected English language.")
    elif message.text == "Russian":
        bot.send_message(message.chat.id, "You selected Russian language.")


def main():
    database = Database(JSONDatabase())
    bot.polling(non_stop=True)


if __name__ == "__main__":
    main()
