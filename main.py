
from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from config import load_config


config = load_config(".env")

bot = Bot(token=config.bot.token)
dp = Dispatcher()
dp['admin_id'] = config.bot.admin_id

# Фильтр на админа
class IsAdmin(BaseFilter):
    def __init__(self, admin_id : int) -> None:
        self.admin_id = admin_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == self.admin_id  # type: ignore
    

# Хэндлер для админа
@dp.message(IsAdmin(dp['admin_id'] ))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


# Хэндлер для всех остальных
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')

if __name__ == "__main__":
    dp.run_polling(bot)
