from ytviewbot.net.proxy_pool import ProxyPool


def test_proxy_pool_skips_comments():
    pool = ProxyPool(["# comment", "http://127.0.0.1:8080", ""])
    assert len(pool) == 1
    assert pool.next() == "http://127.0.0.1:8080"


def test_proxy_pool_empty():
    pool = ProxyPool([])
    assert pool.next() is None
</>