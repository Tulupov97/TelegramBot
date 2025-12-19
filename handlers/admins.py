from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from config.config import load_config
from keyboards.keybords import keyboard, admins_keyboard
from main import bot
from config.config_updater import update_json_env_variable

admins_router = Router()

@admins_router.message(F.text == 'Добавить админа' and F.user_shared)
async def set_admin(message: Message):
    update_json_env_variable('ADMINS_ID', message.user_shared.user_id)
    message.answer(text='Админ добавлен')