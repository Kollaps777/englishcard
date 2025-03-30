# EnglishCard - Telegram-бот для изучения английского

## Описание
Telegram-бот для изучения английского языка с викторинами и персональным словарем. Использует **Python**, **PostgreSQL** и **SQLAlchemy**.

## Установка

### 1. Склонируйте репозиторий:
git clone <ссылка_на_репозиторий>
cd englishcard

### 2. Создайте базу данных:
sudo -u postgres psql -f create_db.sql

### 3. Установите зависимости:
pip install -r requirements.txt

### 4. Настройте токен бота в main.py:
bot = telebot.TeleBot("ВАШ_ТОКЕН")

### 5. Настройте подключение к базе в database.py:
DATABASE_URL = "postgresql://postgres:ВАШ_ПАРОЛЬ@localhost:5432/englishcard_db"

## Зависимости
pyTelegramBotAPI
sqlalchemy
psycopg2-binary

Полный список зависимостей — в файле requirements.txt.

## Запуск
python main.py

## Использование
/start — начать работу с ботом.
/quiz — запустить викторину.
/add — добавить слово (например: cat кошка).
/delete — удалить слово.

