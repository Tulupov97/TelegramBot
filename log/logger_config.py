# logger_config.py
import logging
import os
from datetime import datetime

# Создаём папку для логов, если её нет
logs_dir = "./log/logs"
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Имя файла лога с датой
log_file = os.path.join(logs_dir, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

# Настраиваем логгер
def setup_logger(name="app_logger", level=logging.DEBUG):
    # Создаём логгер с указанным именем
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Проверяем, не добавлены ли уже обработчики (чтобы избежать дублирования)
    if not logger.handlers:
        # Формат сообщений
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Обработчик для записи в файл
        file_handler = logging.FileHandler(log_file, encoding="utf-8", mode="a")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)

        # Обработчик для вывода в консоль (опционально)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level)

        # Добавляем обработчики
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
