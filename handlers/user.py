from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from config.config import load_config
from keyboards.keybords import keyboard, admins_keyboard
from main import bot
from log.logger_config import setup_logger

logger = setup_logger("user.py")



user_router = Router()

# Этот хэндлер срабатывает на команду /start
@user_router.message(CommandStart())
async def process_start_command(message: Message):
    if str(message.from_user.id) not in load_config('.env').bot.admins_id: #type: ignore
        print('user')
        await message.answer(text=f'Привет {message.from_user.full_name}', reply_markup=keyboard) # type: ignore
    else:
        print('admin')
        await message.answer(text=f'Привет {message.from_user.full_name}', reply_markup=admins_keyboard) # type: ignore

@user_router.message(Command(commands="help"))
async def help_command(message: Message):
    await message.answer(text=f"/help\n/start")


# Этот хэндлер будет срабатывать на ...
@user_router.message(F.text == 'Локации общих прогулок')
async def our_location(message: Message):
    await bot.send_location(
        chat_id=message.chat.id,
        latitude=59.867876,
        longitude=30.329685)


