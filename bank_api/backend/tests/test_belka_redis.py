from bank_api.backend.app.apis_all_banks.belarusbank_api.belka_redis import belarusbank_get_from_redis


def test_belka_add_redis():
    data = belarusbank_get_from_redis()
    assert isinstance(data, str)
    assert len(data) > 0