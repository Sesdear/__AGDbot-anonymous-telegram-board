from dataclasses import dataclass

from aiogram import Bot

from bot.config.app_config import AppConfig
from bot.config.settings import Settings
from bot.services.broadcaster import Broadcaster
from bot.services.cooldown import CooldownService
from bot.services.publisher import Publisher
from bot.storage.held_messages import HeldMessageStore
from bot.storage.protocols import PostTracker, SubscriberStore


@dataclass(slots=True)
class AppContext:
    settings: Settings
    app_config: AppConfig
    bot: Bot
    publisher: Publisher
    broadcaster: Broadcaster
    subscribers: SubscriberStore
    post_tracker: PostTracker
    cooldown: CooldownService
    held_messages: HeldMessageStore
