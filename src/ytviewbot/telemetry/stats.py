from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class SessionStats:
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    completed: int = 0
    failed: int = 0
    skipped: int = 0

    def record(self, ok: bool) -> None:
        if ok:
            self.completed += 1
        else:
            self.failed += 1

    def summary(self) -> str:
        return f"completed={self.completed} failed={self.failed} skipped={self.skipped}"