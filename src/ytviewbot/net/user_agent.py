from __future__ import annotations

import itertools
import random
from pathlib import Path

DEFAULT_UA = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/129.0 Safari/537.36",
]


class UserAgentRotator:
    def __init__(self, agents: list[str]) -> None:
        self._agents = agents or DEFAULT_UA
        self._cycle = itertools.cycle(self._agents)

    @classmethod
    def from_settings(cls, path: str = "config/user_agents.txt") -> "UserAgentRotator":
        p = Path(path)
        lines = [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()] if p.exists() else []
        return cls(lines)

    def next(self) -> str:
        return next(self._cycle)

    def random(self) -> str:
        return random.choice(self._agents)