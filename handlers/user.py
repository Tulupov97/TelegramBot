from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from config.config import load_config
from keyboards.inline_keyboards import test_keyboard, inline_keyboard
from log.logger_config import setup_logger

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
    await callback.bot.send_message(
    chat_id=callback.message.chat.id,
    text=f"📍 Открыть на Яндекс.Картах: {yandex_maps_url}",
    disable_web_page_preview=False  # чтобы превью отобразилось
    )

    await callback.answer()