from __future__ import annotations

import tomllib
from functools import lru_cache
from pathlib import Path

from ytviewbot.config.models import Settings

DEFAULT_PATH = Path("config/default.toml")


@lru_cache(maxsize=1)
def load_settings(path: str | Path | None = None) -> Settings:
    cfg_path = Path(path) if path else DEFAULT_PATH
    if not cfg_path.exists():
        return Settings()
    with cfg_path.open("rb") as fh:
        raw = tomllib.load(fh)
    return Settings.model_validate(raw)