from __future__ import annotations

import itertools
from pathlib import Path


class ProxyPool:
    def __init__(self, proxies: list[str], strategy: str = "round_robin") -> None:
        self._proxies = [p for p in proxies if p and not p.startswith("#")]
        self._strategy = strategy
        self._cycle = itertools.cycle(self._proxies) if self._proxies else None

    @classmethod
    def from_settings(cls, pool_file: str = "config/proxies.txt", strategy: str = "round_robin") -> "ProxyPool":
        path = Path(pool_file)
        lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
        return cls(lines, strategy=strategy)

    def next(self) -> str | None:
        if not self._cycle:
            return None
        return next(self._cycle)

    def __len__(self) -> int:
        return len(self._proxies)