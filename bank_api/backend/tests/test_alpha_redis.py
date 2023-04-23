from bank_api.backend.app.apis_all_banks.alpha_api.alpha_redis import alpha_get_from_redis
from bank_api.backend.app.redis.redis_setup import redis_client


def test_alpha_get_from_redis():
    data = alpha_get_from_redis()
    assert isinstance(data, str)


def test_alpha_add_redis():
    getter = redis_client.get("alpha_bank")
    assert isinstance(getter, bytes)
