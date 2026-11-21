# yt-view-bot — Architecture

The bot is split into four layers:

- `src/ytviewbot/config` — pydantic settings loaded from `config/default.toml`.
- `src/ytviewbot/engine` — session lifecycle and parallel dispatcher.
- `src/ytviewbot/net` — proxy pool + user-agent rotation.
- `src/ytviewbot/watchlist` — target parsing from `watchlist.txt`.
- `src/ytviewbot/telemetry` — per-run counters.

The CLI (`ytviewbot.cli`) is the only entrypoint. Each `ViewerSession`
picks a proxy, a user-agent, and a randomized watch duration before
simulating a view using a headless Playwright context.

## Disclaimer

This project is provided for educational and research purposes only.
Running a viewer bot against YouTube violates their Terms of Service.
Use at your own risk.
</>