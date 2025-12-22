from pydantic import BaseModel
from environs import Env, EnvError
import logging

logger = logging.getLogger(__name__)

class TgBot(BaseModel):
    token : str
    admins_id : list[int]

class Config(BaseModel):
    bot : TgBot

def load_config(path: str | None = None) -> Config:
    try:
        env = Env()
        env.read_env(override=True)

        return Config(
        bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admins_id=env.list("ADMINS_ID", subcast=int)))
    
    except FileNotFoundError:
        logger.critical("Конфигурационный файл .env не найден. Проверьте его наличие или переменные окружения.🛑")
        raise
    except EnvError as e:
        logger.critical(f"Ошибка парсинга переменных окружения: {e}. Проверьте корректность .env файла.🛑")
        raise
    except Exception as e:
        logger.critical(f"Неизвестная ошибка при загрузке конфигурации: {e}🛑")
        raise