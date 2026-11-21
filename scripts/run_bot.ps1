# Launch yt-view-bot from a Windows terminal.
$ErrorActionPreference = "Stop"
if (-not (Test-Path ".venv")) {
    python -m venv .venv
}
& .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m ytviewbot run --watchlist watchlist.txt --concurrency 4