import logging

from app.redis.redis_setup import redis_client
from app.apis_all_banks.belarusbank_api.belka_pd import belka_bank_dict
from app.decorators.for_all import dec_for_all_pars_redis

logger = logging.getLogger("bank_aggregator")
URL2 = 'https://belarusbank.by/api/kursExchange'


def belka_add_redis(url: str):
    try:
        data_list = belka_bank_dict(url)
        redis_client.set("belarus_bank", str(data_list))

        logger.info(f"Data from alpha bank was added -- {data_list}")
    except Exception as err:
        logger.info(f"you have error -- {err}")
    finally:
        redis_client.close()
        logger.info("redis bd was closed")


@dec_for_all_pars_redis
def belarusbank_get_from_redis():
    try:
        belka = redis_client.get("belarus_bank")
        logger.info(f"Data get")
        print(belka)
        return eval(belka)
    except Exception as err:
        logger.info(f"you have error -- {err}")
    finally:
        redis_client.close()
        logger.info("redis bd was closed")
