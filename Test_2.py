import logging


format='[{asctime}] #{levelname:8} {filename}:' '{lineno} - {name} - {message}'
formatter = logging.Formatter(format, style='{') 


logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('logs.log')

set_handler_foramter = file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

print(logger.handlers)

logger.warning('Это лог с предупреждением!')