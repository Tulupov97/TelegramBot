from aiogram import Dispatcher, Bot, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from Bot_token import BOT_TOKEN
import json
import os

dp = Dispatcher()
my_bot = Bot(token=BOT_TOKEN)


# Путь к файлу с данными
USERS_FILE = 'users_data.json'


# Функция для загрузки данных пользователей
def load_users():
    if not os.path.exists(USERS_FILE) or os.path.getsize(USERS_FILE) == 0:
        return {}
    with open(USERS_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)


# Функция для сохранения данных пользователей
def save_users(users_data):
    with open(USERS_FILE, 'w', encoding='utf-8') as file:
        json.dump(users_data, file, ensure_ascii=False, indent=4)


@dp.message(CommandStart())
async def start_message_handler(message: Message):
    users_data = load_users()
    user_id = str(message.chat.id)

    if user_id in users_data:
        await message.answer(f'Привет!, {message.chat.first_name}')
    else:
        # Сохраняем username, first_name
        users_data[user_id] = {
            "username": message.chat.username,
            "first_name": message.chat.first_name,
        }
        save_users(users_data)
        await message.answer(f'Здравствуйте, {message.chat.first_name} Добро пожаловать')


@dp.message()
async def all_message_handler(message: Message):
    # Выводим структуру сообщения в консоль (для отладки)
    print(message.model_dump_json(indent=4, exclude_none=True))
    # Отвечаем тем же текстом
    await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(my_bot)
