from __future__ import annotations

from pathlib import Path

from ytviewbot.watchlist.models import WatchTarget


class WatchlistLoader:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def load(self) -> list[WatchTarget]:
        if not self.path.exists():
            return []
        targets: list[WatchTarget] = []
        for raw in self.path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            video_id = self._extract_id(line)
            if video_id:
                targets.append(WatchTarget(video_id=video_id, url=line if line.startswith("http") else None))
        return targets

    @staticmethod
    def _extract_id(line: str) -> str | None:
        if "v=" in line:
            return line.split("v=")[1].split("&")[0]
        if line.startswith("http"):
            return line.rstrip("/").split("/")[-1]
        return line