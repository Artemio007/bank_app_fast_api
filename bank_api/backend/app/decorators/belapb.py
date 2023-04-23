from datetime import datetime


def dec_for_belapb_pars_redis(func):
    def wrapper(*args):
        f = func(*args)
        info = ''
        for i in f:

            info += f"{i.get('sell_currency')} / {i.get('buy_currency')} курс обмена: {i.get('convert')}  "
        return info
    return wrapper


def get_dict_belapb_with_date(func):
    def wrapper(*args):
        f = func(*args)
        for i in range(len(f)):
            f[i]["time_get_data"] = datetime.now()
        return f
    return wrapper