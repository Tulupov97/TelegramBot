
from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from config.config import load_config
import json


config = load_config(".env")

bot = Bot(token=config.bot.token)
dp = Dispatcher()
dp['admins_id'] = config.bot.admins_id

# Фильтр на админа
class IsAdmin(BaseFilter):
    def __init__(self, admins_id : list[int]) -> None:
        self.admins_id = admins_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins_id  # type: ignore
    

# Хэндлер для админа
@dp.message(IsAdmin(dp['admins_id']))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


# Хэндлер для всех остальных
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')

if __name__ == "__main__":
    dp.run_polling(bot)
