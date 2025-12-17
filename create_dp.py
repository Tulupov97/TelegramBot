from aiogram import Dispatcher
from config.config import load_config

dp = Dispatcher()
config = load_config(".env")
dp['admins_id'] = config.bot.admins_id
