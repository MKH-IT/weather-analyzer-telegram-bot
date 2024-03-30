from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_languages_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("English", callback_data="language_english"),
        InlineKeyboardButton("Russian", callback_data="language_russian"),
        InlineKeyboardButton("Uzbek", callback_data="language_uzbek"),
    )
    return markup
