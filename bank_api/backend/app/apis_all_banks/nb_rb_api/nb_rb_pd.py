import requests
from datetime import datetime
from app.decorators.for_all import dec_all_dataframe_sql

URL = " https://www.nbrb.by/api/exrates/rates?periodicity=0"


@dec_all_dataframe_sql(bank_name="nbrb")
def nb_rb_pd(url: str):
    response = requests.get(url)
    cur = response.json()
    info = []
    for i in cur:
        info.append({"sell_currency": "BYN", "buy_currency": i.get("Cur_Abbreviation"),
                     "convert": float(i.get("Cur_OfficialRate")), "time_get_data": datetime.now()})
    return info

