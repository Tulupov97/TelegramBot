from aiogram.types import Message
from aiogram import Router, F
from config.config import load_config
from keyboards.keybords import keyboard, admins_keyboard



admins_router = Router()

@admins_router.message(F.text == 'Добавить админа')
async def set_admin(message: Message):
    ...
    message.answer(text='Админ добавлен')