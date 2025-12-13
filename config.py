from pydantic import BaseModel
from environs import Env


class TgBot(BaseModel):
    token : str
    admin_id : int


class Config(BaseModel):
    bot : TgBot


def load_config(path : str) -> Config:

    env = Env()
    env.read_env(override=True)

    return Config(bot = TgBot(token=env("BOT_TOKEN"), admin_id = env("ADMIN_ID")))