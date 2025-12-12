
from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram import Bot, Dispatcher
import os, dotenv, json
import environs


env = environs.Env()
env.read_env()

bot = Bot(token=env('BOT_TOKEN'))
dp = Dispatcher()

#фильтр на админа
class IsAdmin(BaseFilter):
    def __init__(self, admin_id : int) -> None:
        self.admin_id = admin_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id is self.admin_id
    

# Этот хэндлер будет срабатывать, если апдейт от админа
@dp.message(IsAdmin(env.int("ADMIN_ID")))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


# Этот хэндлер будет срабатывать, если апдейт не от админа
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')

print(os.getenv('BOT_TOKEN'))
print(os.getenv('ADMIN_ID'))