from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем кнопки
location_btn = KeyboardButton(
    text='Локации общих прогулок')

# Добавляем кнопки
kb_builder.row(location_btn, width=2)

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True)