from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from config.config import load_config
from keyboards.keybords import keyboard, admins_keyboard
from keyboards.inline_keyboards import base_keyboard
from main import bot
from log.logger_config import setup_logger

logger = setup_logger("user.py")



user_router = Router()

# Этот хэндлер срабатывает на команду /start
@user_router.message(CommandStart())
async def process_start_command(message: Message):
    if message.from_user.id not in load_config('.env').bot.admins_id: #type: ignore
        await message.answer(text=f'Привет {message.from_user.full_name}', reply_markup=keyboard) # type: ignore
    else:
        await message.answer(text=f'Привет {message.from_user.full_name}', reply_markup=admins_keyboard) # type: ignore

@user_router.message(Command(commands="help"))
async def help_command(message: Message):
    await message.answer(text=f"None")

@user_router.message(Command(commands="other"))
async def other_command(message: Message):
    await message.answer(text=f"Группу моей девушки😆", reply_markup=base_keyboard)


# Этот хэндлер будет срабатывать на ...
@user_router.callback_query(F.data == 'Локации совместных прогулок')
async def our_location(callback: CallbackQuery):
    await callback.bot.send_location( # type: ignore
        chat_id=callback.message.chat.id, # type: ignore
        latitude=59.867876,
        longitude=30.329685) 
    await callback.answer()