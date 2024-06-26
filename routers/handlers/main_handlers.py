from aiogram import Router, types
from aiogram.enums import ChatAction
from aiogram.utils.chat_action import ChatActionSender
import main.main as main_func


router = Router(name=__name__)


@router.message()
async def question(message: types.Message):
    action_sender = ChatActionSender(bot=message.bot,
                                     chat_id=message.chat.id,
                                     interval=2,
                                     action=ChatAction.UPLOAD_VIDEO)
    async with action_sender:
        gif, answer = await main_func.yes_or_no()
        await message.answer_animation(animation=gif, caption=answer)
