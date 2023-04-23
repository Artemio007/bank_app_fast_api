import requests
from app.decorators.for_all import dec_all_dataframe_sql
from app.decorators.belka import dict_from_belarusbank, dict_from_belarusbank_without_date

URL2 = 'https://belarusbank.by/api/kursExchange'

bank_name = "belarusbank"


@dec_all_dataframe_sql(bank_name)
@dict_from_belarusbank
def belka_bank(url: str):
    response = requests.get(url)
    json_file = response.json()
    diction = {}
    num = 0
    for item in json_file[0].items():
        num += 1
        currency, rate = item
        c = {currency.replace('_in', ' продажа').replace('_out', ' покупка'): rate}
        diction.update(c)
    d = str(diction)
    l = d[0:733] + "}"
    end_dict = eval(l)
    new_dict = {key: value for key, value in end_dict.items() if value != "0.0000"}
    return new_dict


@dict_from_belarusbank_without_date
def belka_bank_dict(url: str):
    response = requests.get(url)
    json_file = response.json()
    diction = {}
    num = 0
    for item in json_file[0].items():
        num += 1
        currency, rate = item
        c = {currency.replace('_in', ' продажа').replace('_out', ' покупка'): rate}
        diction.update(c)
    d = str(diction)
    l = d[0:733] + "}"
    end_dict = eval(l)
    new_dict = {key: value for key, value in end_dict.items() if value != "0.0000"}
    return new_dict
