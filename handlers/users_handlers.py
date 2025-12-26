from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from config.config import load_config
from log.logger_config import setup_logger
from callback_data_factory import CallbackDataFactory

logger = setup_logger("user.py")

user_router = Router()


# Этот хэндлер будет срабатывать на ...
@user_router.callback_query(F.data == 'Локации совместных прогулок')
async def our_location(callback: CallbackQuery):

    await callback.bot.send_location( # type: ignore
        chat_id=callback.message.chat.id, # type: ignore
        latitude=59.867876,
        longitude=30.329685)
    yandex_maps_url = f"https://yandex.ru/maps/?ll={30.329685},{59.867876}&z=17&pt={30.329685},{59.867876}&l=nkarusk"
    await callback.bot.send_message( # type: ignore
    chat_id=callback.message.chat.id, # type: ignore
    text=f"📍 Открыть на Яндекс.Картах: {yandex_maps_url}",
    disable_web_page_preview=False  # чтобы превью отобразилось
    )
    await callback.answer()

@user_router.callback_query(CallbackDataFactory.filter())
async def callback_query(callback: CallbackQuery, callback_data: CallbackDataFactory):
    await callback.message.answer( # type: ignore
        text=f'Страна {callback_data.country}\n'\
             f'Область: {callback_data.region}\n'\
             f'Город: {callback_data.city}'
    )
    await callback.answer()