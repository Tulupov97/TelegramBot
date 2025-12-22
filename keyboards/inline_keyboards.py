from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lena_group_btn = InlineKeyboardButton(text='Группа "Ленка в меде"', url='https://t.me/chernositovalenaa')
location_btn = InlineKeyboardButton(text='Локации совместных прогулок', callback_data='Локации совместных прогулок')


test_keyboard = InlineKeyboardMarkup(inline_keyboard=[[lena_group_btn]])
inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[location_btn]])
