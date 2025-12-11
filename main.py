
from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram import Bot, Dispatcher
import os

from is_admin_data import admins_id_list
from bot_token import BOT_TOKEN



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#фильтр на админа
class IsAdmin(BaseFilter):
    def __init__(self, admins_id_list : list[int]) -> None:
        self.admins_id_list = admins_id_list

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins_id_list

# Этот хэндлер будет срабатывать, если апдейт от админа
@dp.message(IsAdmin(admins_id_list))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


# Этот хэндлер будет срабатывать, если апдейт не от админа
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')


