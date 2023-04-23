from bank_api.backend.app.apis_all_banks.nb_rb_api.nb_rb_pd import nb_rb_pd, URL


def test_nb_rb_bank():
    assert nb_rb_pd(URL) is None