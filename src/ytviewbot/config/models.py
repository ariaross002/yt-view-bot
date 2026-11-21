from __future__ import annotations

from pydantic import BaseModel, Field


class BotSection(BaseModel):
    name: str = "yt-view-bot"
    engine: str = "playwright"
    default_watch_seconds: int = 45
    max_concurrent_sessions: int = 4
    headless: bool = True
    rotate_user_agent: bool = True
    randomize_referrer: bool = True


class ProxySection(BaseModel):
    enabled: bool = True
    pool_file: str = "config/proxies.txt"
    strategy: str = "round_robin"
    retry_on_fail: int = 3


class ThrottleSection(BaseModel):
    min_delay_ms: int = 800
    max_delay_ms: int = 4200
    jitter: bool = True


class LoggingSection(BaseModel):
    level: str = "INFO"
    file: str = "logs/yt-view-bot.log"
    rotate_mb: int = 10


class Settings(BaseModel):
    bot: BotSection = Field(default_factory=BotSection)
    proxy: ProxySection = Field(default_factory=ProxySection)
    throttle: ThrottleSection = Field(default_factory=ThrottleSection)
    logging: LoggingSection = Field(default_factory=LoggingSection)