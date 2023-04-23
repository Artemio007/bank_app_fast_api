import requests
import logging
from app.redis.redis_setup import redis_client


logger = logging.getLogger("bank_aggregator")
URL = " https://www.nbrb.by/api/exrates/rates?periodicity=0"


def nb_rb_redis(url: str = URL):
    response = requests.get(url)
    cur = response.json()
    info = ''
    for i in cur:
        info += f"{i.get('Cur_Abbreviation')} {i.get('Cur_Name')} = {i.get('Cur_OfficialRate')} BYN  "
    return info


def nb_rb_add_redis(url: str):
    try:
        data_str = nb_rb_redis(url)
        redis_client.set("nb_rb", data_str)
        logger.info(f"Data from nb_rb bank was added -- {data_str}")
    except Exception as err:
        logger.info(f"you have error -- {err}")
    finally:
        redis_client.close()
        logger.info("redis bd was closed")


def nb_rb_get_from_redis():
    try:
        nb_rb = redis_client.get("nb_rb")
        logger.info(f"Data get")
        string_data = nb_rb.decode('utf-8')
        # return eval(nb_rb)
        return string_data
    except Exception as err:
        logger.info(f"you have error -- {err}")
    finally:
        redis_client.close()
        logger.info("redis bd was closed")


