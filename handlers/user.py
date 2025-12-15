from main import dp
from aiogram.types import Message

# Хэндлер для всех остальных
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')