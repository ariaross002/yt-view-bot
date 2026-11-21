# Package the bot as a single-file Windows executable.
$ErrorActionPreference = "Stop"
pip install pyinstaller
pyinstaller --name yt-view-bot --onefile --noconsole src\ytviewbot\__main__.py
Write-Host "Built dist\yt-view-bot.exe"