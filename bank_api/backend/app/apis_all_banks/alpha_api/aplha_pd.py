import requests

from app.decorators.alpha import get_dict_from_alpha_without_date, get_dict_from_alpha
from app.decorators.for_all import dec_all_dataframe_sql

bank_name = "alphabank"
URL1 = 'https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates'


@dec_all_dataframe_sql(bank_name)
@get_dict_from_alpha
def alpha(url: str):
    response = requests.get(url)
    json_file = response.json()
    data_list = json_file.get("rates")
    return data_list


@get_dict_from_alpha_without_date
def alpha_dict(url: str):
    response = requests.get(url)
    json_file = response.json()
    data_list = json_file.get("rates")
    return data_list
