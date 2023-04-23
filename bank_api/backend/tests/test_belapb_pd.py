from bank_api.backend.app.apis_all_banks.belapb_api.belapb_pd import belapb_bank, helper


def test_belapb_bank():
    assert belapb_bank(helper) is None