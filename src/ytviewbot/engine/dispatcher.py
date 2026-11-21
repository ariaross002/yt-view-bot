from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed

from loguru import logger

from ytviewbot.config.models import Settings
from ytviewbot.engine.session import ViewerSession
from ytviewbot.watchlist.models import WatchTarget


class ViewDispatcher:
    def __init__(self, settings: Settings, concurrency: int = 4) -> None:
        self.settings = settings
        self.concurrency = max(1, concurrency)

    def dispatch(self, targets: list[WatchTarget]) -> dict[str, bool]:
        results: dict[str, bool] = {}
        with ThreadPoolExecutor(max_workers=self.concurrency) as pool:
            futures = {
                pool.submit(ViewerSession(t.video_id, self.settings).run): t
                for t in targets
            }
            for fut in as_completed(futures):
                target = futures[fut]
                try:
                    results[target.video_id] = fut.result()
                except Exception as exc:  # noqa: BLE001
                    logger.error("dispatch error {}: {}", target.video_id, exc)
                    results[target.video_id] = False
        return results