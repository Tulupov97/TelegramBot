from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from callback_data_factory import CallbackDataFactory


#клава без билдера
location_btn = InlineKeyboardButton(text='Локации совместных прогулок', callback_data='Локации совместных прогулок')
inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[location_btn]])



#билдер и кнопки
builder = InlineKeyboardBuilder()

builder.button(text= 'Группа "Ленка в меде', url='https://t.me/chernositovalenaa')

builder.button(text= 'Питер', callback_data=CallbackDataFactory(
        country='Russia',
        region='Leningrad region',
        city='Saint-Petersburg'))

builder.button(text="Москва",
    callback_data=CallbackDataFactory(
        country='Russia',
        region='Moscow oblast',
        city='Moscow'))

builder.adjust(1)


