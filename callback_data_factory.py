from aiogram.filters.callback_data import CallbackData

class CallbackDataFactory(CallbackData, prefix = 'location', sep = '|'):
    country: str
    region : str
    city : str


