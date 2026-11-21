from __future__ import annotations

import random
import time
from dataclasses import dataclass, field

from loguru import logger

from ytviewbot.config.models import Settings
from ytviewbot.net.proxy_pool import ProxyPool
from ytviewbot.net.user_agent import UserAgentRotator


@dataclass
class ViewerSession:
    """A single simulated viewer: one browser context, one video, one watch window."""

    video_id: str
    settings: Settings
    proxy_pool: ProxyPool = field(default_factory=ProxyPool.from_settings)
    ua_rotator: UserAgentRotator = field(default_factory=UserAgentRotator.from_settings)

    def run(self) -> bool:
        proxy = self.proxy_pool.next() if self.settings.proxy.enabled else None
        ua = self.ua_rotator.next() if self.settings.bot.rotate_user_agent else None
        watch = self.settings.bot.default_watch_seconds + random.randint(-5, 15)
        logger.info("session start video={} proxy={} ua={}", self.video_id, proxy, ua)
        try:
            time.sleep(watch)
            logger.info("session done video={} watched={}s", self.video_id, watch)
            return True
        except Exception as exc:  # noqa: BLE001
            logger.warning("session failed video={} err={}", self.video_id, exc)
            return False