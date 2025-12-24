from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router
from keyboards.inline_keyboards import builder, inline_keyboard
from config.config import load_config

command_router = Router()


# Этот хэндлер срабатывает на команду /start
@command_router.message(CommandStart())
async def process_start_command(message: Message):
    if message.from_user.id not in load_config().bot.admins_id: #type: ignore
        await message.answer(text=f'Привет {message.from_user.full_name}', reply_markup=inline_keyboard) # type: ignore
    else:
        await message.answer(text=f'Привет {message.from_user.full_name}. Напоминаю - ты админ!', reply_markup=inline_keyboard) # type: ignore

@command_router.message(Command(commands="help"))
async def help_command(message: Message):
    await message.answer(text=f"None")

@command_router.message(Command(commands="test"))
async def other_command(message: Message):
    await message.answer(text=f"Группу моей девушки😆/n и пару тестов", reply_markup=builder.as_markup())