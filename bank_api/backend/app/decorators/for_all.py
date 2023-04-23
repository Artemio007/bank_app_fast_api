import pandas as pd
from app.db.db_setup import engine, async_session_maker, engine_pd


def dec_all_dataframe_sql(bank_name):
    def dec_with_arg(func):
        def wrapper(*args):
            f = func(*args)
            df = pd.DataFrame(f)
            df.to_sql(bank_name, engine_pd, index=False, if_exists='append')
        return wrapper
    return dec_with_arg


def dec_for_all_pars_redis(func):
    def wrapper(*args):
        f = func(*args)
        info = ''
        for i in f:
            info += f"{i.get('sell_currency')} / {i.get('buy_currency')} покупка:{i.get('bank_sell')}, продажа: {i.get('bank_buy')}  "
        return info
    return wrapper
