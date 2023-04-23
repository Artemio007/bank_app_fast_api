from datetime import datetime


def dict_from_belarusbank(func):
    def wrapper(*args):
        a = func(*args)
        inf_list = [dict(list(a.items())[i:i + 2]) for i in range(0, len(a), 2)]
        info_list = []
        for i in inf_list:
            val = list(i.items())
            if len(val[0][0]) < 15:
                between = {"bank_sell": val[0][1], "bank_buy": val[1][1], "sell_currency": "BYN",
                           "buy_currency": val[0][0][0: 3], "time_get_data": datetime.now()}
            else:
                between = {"bank_sell": val[0][1], "bank_buy": val[1][1], "sell_currency": val[0][0][0: 3],
                           "buy_currency": val[0][0][4: 7], "time_get_data": datetime.now()}
            info_list.append(between)
        return info_list
    return wrapper


def dict_from_belarusbank_without_date(func):
    def wrapper(*args):
        a = func(*args)
        inf_list = [dict(list(a.items())[i:i + 2]) for i in range(0, len(a), 2)]
        info_list = []
        for i in inf_list:
            val = list(i.items())
            if len(val[0][0]) < 15:
                between = {"bank_sell": val[0][1], "bank_buy": val[1][1], "sell_currency": "BYN",
                           "buy_currency": val[0][0][0: 3]}
            else:
                between = {"bank_sell": val[0][1], "bank_buy": val[1][1], "sell_currency": val[0][0][0: 3],
                           "buy_currency": val[0][0][4: 7]}
            info_list.append(between)
        return info_list
    return wrapper