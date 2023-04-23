import logging

from app.redis.redis_setup import redis_client
from app.apis_all_banks.alpha_api.aplha_pd import alpha_dict
from app.decorators.for_all import dec_for_all_pars_redis


logger = logging.getLogger("bank_aggregator")
URL1 = 'https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates'


def alpha_add_redis(url: str):
    try:
        data_list = alpha_dict(url)
        redis_client.set("alpha_bank", str(data_list))

        logger.info(f"Data from alpha bank was added -- {data_list}")
    except Exception as err:
        logger.info(f"you have error -- {err}")
    finally:
        redis_client.close()
        logger.info("redis bd was closed")


@dec_for_all_pars_redis
def alpha_get_from_redis():
    try:
        alpha = redis_client.get("alpha_bank")
        logger.info(f"Data get")
        # print(eval(alpha))
        return eval(alpha)
    except Exception as err:
        logger.info(f"you have error -- {err}")
    finally:
        redis_client.close()
        logger.info("redis bd was closed")

