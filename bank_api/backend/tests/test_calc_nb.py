from bank_api.backend.app.currensy_calc.calc_nb import calc, all_values, name_all_curr


def test_calc():
    data = calc("BYN", "AUD", 20.2)
    assert isinstance(data, float)
    assert data > 0


def test_all_values():
    data = all_values(name_all_curr, "AUD", 21)
    assert isinstance(data, list)
    assert len(data) > 0