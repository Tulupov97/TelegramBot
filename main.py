from aiogram.types import Message
from aiogram import Bot, Dispatcher
from config.config import load_config
from log.logger_config import setup_logger
from filters.is_admin import IsAdmin


config = load_config(".env")

logger = setup_logger('main.py')

bot = Bot(token=config.bot.token)
dp = Dispatcher()
dp['admins_id'] = config.bot.admins_id


# Хэндлер для всех остальных
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')

if __name__ == "__main__":
    logger.info("Приложение запускается")
    dp.run_polling(bot)
