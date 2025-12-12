import logging

logger = logging.getLogger(__name__)

format = (
    '#{levelname:8} [{asctime}] {filename}:'
    '{lineno} - {name} - {message}')

formatter = logging.Formatter(fmt=format, style='{')

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('logs.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

