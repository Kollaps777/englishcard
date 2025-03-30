from sqlalchemy import create_engine, Column, Integer, String, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

# Настройка подключения к базе данных
DATABASE_URL = "postgresql://postgres:your_password@localhost:5432/englishcard_db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Определение моделей
class User(Base):
    __tablename__ = "users"
    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(255))
    user_words = relationship("UserWord", back_populates="user")

class Word(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True, autoincrement=True)
    english_word = Column(String(50), nullable=False)
    russian_translation = Column(String(50), nullable=False)
    category = Column(String(50))

class UserWord(Base):
    __tablename__ = "user_words"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    english_word = Column(String(50), nullable=False)
    russian_translation = Column(String(50), nullable=False)
    user = relationship("User", back_populates="user_words")

# Создание таблиц в базе данных
Base.metadata.create_all(engine)

# Настройка сессии
Session = sessionmaker(bind=engine)

class Database:
    def __init__(self):
        self.session = Session()

    def add_user(self, user_id, username):
        user = self.session.query(User).filter_by(user_id=user_id).first()
        if not user:
            new_user = User(user_id=user_id, username=username)
            self.session.add(new_user)
            self.session.commit()

    def get_random_word(self):
        # Получение случайного слова из общей таблицы
        word = self.session.query(Word).order_by(func.random()).first()
        return {"english_word": word.english_word, "russian_translation": word.russian_translation}

    def add_user_word(self, user_id, english_word, russian_translation):
        new_word = UserWord(user_id=user_id, english_word=english_word, russian_translation=russian_translation)
        self.session.add(new_word)
        self.session.commit()

    def delete_user_word(self, user_id, english_word):
        self.session.query(UserWord).filter_by(user_id=user_id, english_word=english_word).delete()
        self.session.commit()

    def get_user_word_count(self, user_id):
        return self.session.query(UserWord).filter_by(user_id=user_id).count()

    def close(self):
        self.session.close()

# Инициализация начальных данных (10 слов)
def init_words():
    session = Session()
    if session.query(Word).count() == 0:
        initial_words = [
            Word(english_word="red", russian_translation="красный", category="colors"),
            Word(english_word="blue", russian_translation="синий", category="colors"),
            Word(english_word="green", russian_translation="зеленый", category="colors"),
            Word(english_word="I", russian_translation="я", category="pronouns"),
            Word(english_word="you", russian_translation="ты", category="pronouns"),
            Word(english_word="he", russian_translation="он", category="pronouns"),
            Word(english_word="she", russian_translation="она", category="pronouns"),
            Word(english_word="black", russian_translation="черный", category="colors"),
            Word(english_word="white", russian_translation="белый", category="colors"),
            Word(english_word="they", russian_translation="они", category="pronouns"),
        ]
        session.add_all(initial_words)
        session.commit()
    session.close()