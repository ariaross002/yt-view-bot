# Contributing to yt-view-bot

Thanks for your interest. This is a hobby project — keep PRs focused.

## Local setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m ytviewbot doctor
```

## Style

- Python 3.12, type-hinted, `loguru` for logging.
- Keep feature modules under `src/ytviewbot/<area>/`.
- New engines go in `src/ytviewbot/engine/` and register in the dispatcher.

## Legal

This tool is for educational use only. Do not use it against channels or
videos you do not own. Opening a PR means you accept responsibility for
how you run it.