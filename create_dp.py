from aiogram import Dispatcher
from config.config import load_config
from handlers import user, admins, command_handlers
from keyboards.set_menu import set_default_menu

dp = Dispatcher()
config = load_config()
dp['admins_id'] = config.bot.admins_id

dp.include_router(user.user_router)
dp.include_router(admins.admins_router)
dp.include_router(command_handlers.command_router)
dp.startup.register(set_default_menu)