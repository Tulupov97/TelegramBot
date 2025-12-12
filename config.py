from pydantic import BaseModel
from environs import Env

Env.read_env(override=True)

env = Env()

class TgBot(BaseModel):
    token : str = env("BOT_TOEKN")
    admin_id : int = env("ADMIN_ID")