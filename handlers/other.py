from filters.is_admin import IsAdmin
from main import dp
from aiogram.types import Message

# Хэндлер для админа
@dp.message(IsAdmin(dp['admins_id']))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')