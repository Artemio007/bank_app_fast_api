import datetime

import requests
import xml.etree.ElementTree as ET
import logging

from app.redis.redis_setup import redis_client
from app.decorators.belapb import dec_for_belapb_pars_redis

logger = logging.getLogger("bank_aggregator")

helper = "https://belapb.by/CashConvRatesDaily.php?ondate=04/14/2023"

date_request = datetime.datetime.today().strftime("%m/%d/%Y")
URL3 = f'http://belapb.by/CashConvRatesDaily.php?ondate={date_request}'


def belapb_bank(url: str):
    response = requests.get(url, verify=False)
    root = ET.fromstring(response.content)

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


def belapb_add_redis(url: str):
    try:
        data_list = belapb_bank(url)
        redis_client.set("belapb_bank", str(data_list))

        logger.info(f"Data from belapb bank was added -- {data_list}")
    except Exception as err:
        logger.info(f"you have error -- {err}")
    finally:
        redis_client.close()
        logger.info("redis bd was closed")


@dec_for_belapb_pars_redis
def belapb_get_from_redis():
    try:
        belapb = redis_client.get("belapb_bank")
        logger.info(f"Data get")
        return eval(belapb)
    except Exception as err:
        logger.info(f"you have error -- {err}")
    finally:
        redis_client.close()
        logger.info("redis bd was closed")


