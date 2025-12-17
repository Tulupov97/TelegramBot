from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
#from filters import is_admin
from config.config import load_config
from keyboards.keybords import keyboard
from main import bot



user_router = Router()

# Этот хэндлер срабатывает на команду /start
@user_router.message(CommandStart())
async def process_start_command(message: Message):

    await message.answer(text=f'Привет {message.from_user.full_name}', reply_markup=keyboard) # type: ignore

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


