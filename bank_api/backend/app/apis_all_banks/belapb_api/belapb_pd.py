import datetime

import requests
import xml.etree.ElementTree as ET
import logging

from app.decorators.belapb import get_dict_belapb_with_date
from app.decorators.for_all import dec_all_dataframe_sql


logger = logging.getLogger("bank_aggregator")
helper = "https://belapb.by/CashConvRatesDaily.php?ondate=04/14/2023"

date_request = datetime.datetime.today().strftime("%m/%d/%Y")

URL3 = f'http://belapb.by/CashConvRatesDaily.php?ondate={date_request}'


@dec_all_dataframe_sql(bank_name="belapb")
@get_dict_belapb_with_date
def belapb_bank(url: str):
    root = ET.fromstring(requests.get(url, verify=False).content)
    count = 0
    currency_list = []
    for child in root:
        if count < 11:
            sell_currency = [element.text for element in child.iter('CurrSrc')]
            buy_currency = [element.text for element in child.iter('CurrTrg')]
            convert = [element.text for element in child.iter('ConvRate')]
            curr_dict = {"sell_currency": sell_currency[0], "buy_currency": buy_currency[0], "convert": float(convert[0])}
            currency_list.append(curr_dict)
            count += 1
    return currency_list


