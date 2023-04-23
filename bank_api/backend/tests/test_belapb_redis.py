from bank_api.backend.app.apis_all_banks.belapb_api.belapb_redis import belapb_bank, helper
from bank_api.backend.app.redis.redis_setup import redis_client


def test_belapb_bank():
    data = belapb_bank(helper)
    assert isinstance(data, list)
    assert len(data) > 0


def test_belapb_add_redis():
    data = redis_client.get("alpha_bank")
    assert isinstance(data, bytes)
    assert len(data) > 0