from bank_api.backend.app.decorators.alpha import get_dict_from_alpha_without_date, get_dict_from_alpha
from bank_api.backend.app.apis_all_banks.alpha_api.aplha_pd import alpha, alpha_dict, URL1


def test_alpha():
    data = alpha(URL1)
    assert data is None


def test_get_dict_from_alpha():
    data = get_dict_from_alpha(alpha_dict)(URL1)
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_dict_from_alpha_without_date():
    data = get_dict_from_alpha_without_date(alpha_dict)(URL1)
    assert isinstance(data, list)
    assert len(data) > 0
