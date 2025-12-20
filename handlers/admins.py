from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from config.config import load_config
from keyboards.keybords import keyboard, admins_keyboard
from main import bot


admins_router = Router()

@admins_router.message(F.text == 'Добавить админа' and F.user_shared)
async def set_admin(message: Message):
    ...
    message.answer(text='Админ добавлен')