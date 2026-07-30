import logging

from aiogram import Router
from aiogram.types import Message

from bot.context import AppContext

logger = logging.getLogger(__name__)

router = Router(name="channel")


@router.channel_post()
async def handle_channel_post(message: Message, ctx: AppContext) -> None:
    await ctx.broadcaster.broadcast_channel_post(message.message_id)
