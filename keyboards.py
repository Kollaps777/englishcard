from telebot import types

def create_quiz_keyboard(correct_answer, options):
    keyboard = types.InlineKeyboardMarkup()
    for option in options:
        callback = "correct" if option == correct_answer else "wrong"
        keyboard.add(types.InlineKeyboardButton(text=option, callback_data=callback))
    return keyboard