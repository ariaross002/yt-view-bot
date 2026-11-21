from ytviewbot.watchlist.loader import WatchlistLoader
from ytviewbot.watchlist.models import WatchTarget


def test_extract_bare_id():
    assert WatchlistLoader._extract_id("dQw4w9WgXcQ") == "dQw4w9WgXcQ"


def test_extract_from_url():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=10"
    assert WatchlistLoader._extract_id(url) == "dQw4w9WgXcQ"


def test_target_resolved_url():
    t = WatchTarget(video_id="dQw4w9WgXcQ")
    assert "watch?v=dQw4w9WgXcQ" in t.resolved_url