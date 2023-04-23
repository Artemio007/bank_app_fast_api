from bank_api.backend.app.apis_all_banks.belarusbank_api.belka_pd import belka_bank_dict, belka_bank, URL2


def test_belapb_bank():
    assert belka_bank(URL2) is None


def test_belka_bank_dict():
    date = belka_bank_dict(URL2)
    assert isinstance(date, list)
    assert len(date) > 0
