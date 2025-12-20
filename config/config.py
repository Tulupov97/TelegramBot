from pydantic import BaseModel
from environs import Env

class TgBot(BaseModel):
    token : str
    admins_id : list[int]

class Config(BaseModel):
    bot : TgBot

def load_config(path: str | None = None) -> Config:

    env = Env()
    env.read_env(override=True)

    return Config(
    bot=TgBot(
        token=env.str("BOT_TOKEN"),
        admins_id=env.list("ADMINS_ID", subcast=int)))