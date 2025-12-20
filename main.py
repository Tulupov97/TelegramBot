from aiogram import Bot
from config.config import load_config
from log.logger_config import setup_logger
from create_dp import dp
import asyncio
from handlers import user

config = load_config()
logger = setup_logger('main.py')
bot = Bot(token=config.bot.token)

async def main():
    try:
        await bot.get_me()
        dp.include_router(user.user_router)
        logger.info("Бот запущен ✅")
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as err:
        logger.critical(f"{err}")
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Бот остановлен вручную")