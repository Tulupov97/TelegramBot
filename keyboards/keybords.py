from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup, KeyboardButtonRequestUser)
from aiogram.utils.keyboard import ReplyKeyboardBuilder 
from filters.is_admin import IsAdmin
from config.config import load_config


# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()
admins_kb_bilder = ReplyKeyboardBuilder()

# Создаем кнопки
location_btn = KeyboardButton(
    text='Локации общих прогулок')
set_admin = KeyboardButton(text='Добавить админа', request_user=KeyboardButtonRequestUser(request_id=42))

# Добавляем кнопки
kb_builder.row(location_btn, width=2)
admins_kb_bilder.row(location_btn, set_admin, width=2)

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True)
admins_keyboard: ReplyKeyboardMarkup = admins_kb_bilder.as_markup(resize_keyboard=True)


