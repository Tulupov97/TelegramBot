from pydantic import BaseModel
from environs import Env
import json

class TgBot(BaseModel):
    token : str
    admins_id : list[str]

class Config(BaseModel):
    bot : TgBot

def load_config(path : str) -> Config:

    env = Env()
    env.read_env(override=True)

    return Config(bot = TgBot(token=env("BOT_TOKEN"), admins_id = json.loads(env("ADMINS_ID"))))

