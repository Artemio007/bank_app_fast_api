from datetime import datetime


def get_dict_from_alpha(func):
    def wrapper(*args):
        f = func(*args)
        info = []
        for i in f:
            betw = {"bank_sell": i.get('sellRate'), "bank_buy": i.get('buyRate'), "sell_currency": i.get('sellIso'),
                    "buy_currency": i.get('buyIso'), "time_get_data": datetime.now()}
            info.append(betw)
        return info
    return wrapper


def get_dict_from_alpha_without_date(func):
    def wrapper(*args):
        f = func(*args)
        info = []
        for i in f:
            betw = {"bank_sell": i.get('sellRate'), "bank_buy": i.get('buyRate'), "sell_currency": i.get('sellIso'),
                    "buy_currency": i.get('buyIso')}
            info.append(betw)
        return info
    return wrapper


def dec_for_alpha_pars(func):
    def wrapper(*args):
        f = func(*args)
        info = ''
        for i in f:
            info += f"{i.get('sellIso')} / {i.get('buyIso')} покупка:{i.get('sellRate')}, продажа: {i.get('buyRate')}  "
        return info
    return wrapper

