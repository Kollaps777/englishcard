EnglishCard - Telegram-бот для изучения английского
Описание
Telegram-бот для изучения английского языка с викторинами и персональным словарем. Использует Python, PostgreSQL и SQLAlchemy.

Установка
Склонируйте репозиторий:
bash

Свернуть

Перенос

Копировать
git clone <ссылка_на_репозиторий>
cd englishcard
Создайте базу данных:
bash

Свернуть

Перенос

Копировать
sudo -u postgres psql -f create_db.sql
Установите зависимости:
bash

Свернуть

Перенос

Копировать
pip install -r requirements.txt
Настройте токен бота в main.py:
python

Свернуть

Перенос

Копировать
bot = telebot.TeleBot("ВАШ_ТОКЕН")
Настройте подключение к базе в database.py:
python

Свернуть

Перенос

Копировать
DATABASE_URL = "postgresql://postgres:ВАШ_ПАРОЛЬ@localhost:5432/englishcard_db"
Зависимости
pyTelegramBotAPI==4.14.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
См. requirements.txt.

Запуск
bash

Свернуть

Перенос

Копировать
python main.py
Использование
/start — начать работу с ботом.
/quiz — запустить викторину.
/add — добавить слово (например: cat кошка).
/delete — удалить слово.
Что включено?
Краткое описание проекта.
Основные шаги установки (клонирование, создание базы, установка зависимостей, настройка).
Список зависимостей с указанием файла requirements.txt.
Команда для запуска.
Основные команды бота.
