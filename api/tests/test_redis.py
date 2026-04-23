from unittest.mock import patch

@patch("redis.Redis")
def test_redis_mock(mock_redis):
    mock_redis.return_value.ping.return_value = True
    r = mock_redis()
    assert r.ping() is True
