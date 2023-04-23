from bank_api.backend.app.apis_all_banks.nb_rb_api.nb_rb_redis import nb_rb_get_from_redis
from bank_api.backend.app.redis.redis_setup import redis_client


def test_nb_rb_get_from_redis():
    data1 = redis_client.get("nb_rb").decode('utf-8')
    data2 = nb_rb_get_from_redis()
    assert data1 == data2
    assert isinstance(data2, str)
    assert len(data2) > 0