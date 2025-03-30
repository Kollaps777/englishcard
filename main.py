import telebot
import random
from database import Database, init_words
from keyboards import create_quiz_keyboard

bot = telebot.TeleBot("YOUR_BOT_TOKEN")
db = Database()

# Инициализация начальных данных при запуске
init_words()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username
    db.add_user(user_id, username)
    bot.reply_to(message, "Привет! Я бот для изучения английского языка. Нажми /quiz, чтобы начать!")

@bot.message_handler(commands=['quiz'])
def start_quiz(message):
    word = db.get_random_word()
    correct_answer = word['english_word']
    options = [correct_answer]
    while len(options) < 4:
        random_word = db.get_random_word()['english_word']
        if random_word not in options:
            options.append(random_word)
    random.shuffle(options)
    keyboard = create_quiz_keyboard(correct_answer, options)
    bot.send_message(message.chat.id, f"Как переводится '{word['russian_translation']}'?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_answer(call):
    if call.data == "correct":
        bot.answer_callback_query(call.id, "Правильно!")
        bot.send_message(call.message.chat.id, "Молодец! Нажми /quiz для следующего слова.")
    else:
        bot.answer_callback_query(call.id, "Неправильно!")
        bot.send_message(call.message.chat.id, "Попробуй еще раз! Нажми /quiz.")

@bot.message_handler(commands=['add'])
def add_word(message):
    msg = bot.reply_to(message, "Введи слово на английском и его перевод через пробел (например: cat кошка)")
    bot.register_next_step_handler(msg, process_new_word)

def process_new_word(message):
    try:
        english_word, russian_translation = message.text.split(" ", 1)
        db.add_user_word(message.from_user.id, english_word, russian_translation)
        count = db.get_user_word_count(message.from_user.id)
        bot.reply_to(message, f"Слово '{english_word}' добавлено! Всего слов: {count}")
    except ValueError:
        bot.reply_to(message, "Ошибка! Введи слово и перевод через пробел.")

@bot.message_handler(commands=['delete'])
def delete_word(message):
    msg = bot.reply_to(message, "Введи слово на английском, которое хочешь удалить")
    bot.register_next_step_handler(msg, process_delete_word)

def process_delete_word(message):
    english_word = message.text
    db.delete_user_word(message.from_user.id, english_word)
    bot.reply_to(message, f"Слово '{english_word}' удалено (если оно было в твоем списке).")

if __name__ == "__main__":
    try:
        bot.polling()
    finally:
        db.close()  # Закрытие сессии при завершении работы