from app.apis_all_banks.nb_rb_api.nb_rb_redis import nb_rb_get_from_redis

name_all_curr = [
    'BYN', 'AUD', 'AMD', 'BGN', 'BRL', 'UAH', 'DKK',
    'AED', 'USD', 'VND', 'EUR', 'PLN', 'JPY', 'INR',
    'IRR', 'ISK', 'CAD', 'CNY', 'KWD', 'MDL', 'NZD',
    'NOK', 'RUB', 'XDR', 'SGD', 'KGS', 'KZT', 'TRY',
    'GBP', 'CZK', 'SEK', 'CHF',
]


def calc(currency_need: str, currency_have: str, quantity_have):
    list_all = nb_rb_get_from_redis().split("  ")
    dict_val = {'BYN': 1}
    for i in list_all:
        for_up = i.split()
        if for_up:
            if for_up[0] == "RUB" or for_up[0] == "UAH":
                d = dict([(for_up[0], float(for_up[-2]) / 100)])
                dict_val.update(d)
            elif for_up[0] == "PLN":
                d = dict([(for_up[0], float(for_up[-2]) / 10)])
                dict_val.update(d)
            else:
                d = dict([(for_up[0], float(for_up[-2]))])
                dict_val.update(d)
    if currency_have == "BYN":
        conv = dict_val.get(currency_need)
        equal = quantity_have / conv
        return round(equal, 2)

    elif not currency_have == "BYN":
        conv_have = dict_val.get(currency_have)
        cur_have_in_byn = quantity_have * conv_have
        conv_need = dict_val.get(currency_need)
        equal = cur_have_in_byn / conv_need
        return round(equal, 2)


def all_values(val_list: list, need_curr, quantity):
    list_for_temp = []
    for i in val_list:
        c = calc(i, need_curr, quantity)
        list_for_temp.append(f"{c} {i}")
    return list_for_temp





