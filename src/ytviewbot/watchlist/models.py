from __future__ import annotations

from pydantic import BaseModel, Field


class WatchTarget(BaseModel):
    video_id: str = Field(min_length=5, max_length=32)
    url: str | None = None
    watch_seconds: int | None = None
    enabled: bool = True

    @property
    def resolved_url(self) -> str:
        return self.url or f"https://www.youtube.com/watch?v={self.video_id}"