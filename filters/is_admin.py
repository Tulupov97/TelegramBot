from aiogram.filters import BaseFilter
from aiogram.types import Message 

# Фильтр на админа
class IsAdmin(BaseFilter):
    def __init__(self, admins_id : list[int]) -> None:
        self.admins_id = admins_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins_id  # type: ignore