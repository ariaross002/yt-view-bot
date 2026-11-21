from __future__ import annotations

import typer
from rich.console import Console

from ytviewbot.config.loader import load_settings
from ytviewbot.engine.dispatcher import ViewDispatcher
from ytviewbot.watchlist.loader import WatchlistLoader

app = typer.Typer(help="yt-view-bot — desktop Youtube viewer bot.")
console = Console()


@app.command()
def run(watchlist: str = typer.Option("watchlist.txt", help="Path to watchlist file."),
        concurrency: int = typer.Option(4, help="Parallel browser sessions.")) -> None:
    settings = load_settings()
    targets = WatchlistLoader(watchlist).load()
    console.print(f"[bold]Loaded[/] {len(targets)} target video(s)")
    dispatcher = ViewDispatcher(settings=settings, concurrency=concurrency)
    dispatcher.dispatch(targets)


@app.command()
def doctor() -> None:
    settings = load_settings()
    console.print(f"engine = {settings.bot.engine}")
    console.print(f"headless = {settings.bot.headless}")
    console.print(f"proxies = {settings.proxy.pool_file}")


if __name__ == "__main__":
    app()