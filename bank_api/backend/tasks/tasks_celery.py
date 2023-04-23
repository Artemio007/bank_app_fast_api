from celery import Celery

import logging

from app.apis_all_banks.belarusbank_api.belka_redis import belka_add_redis, URL2
from app.apis_all_banks.alpha_api.alpha_redis import alpha_add_redis, URL1
from app.apis_all_banks.nb_rb_api.nb_rb_redis import nb_rb_add_redis, URL
from app.apis_all_banks.belapb_api.belapb_redis import belapb_add_redis, URL3, helper

from run_db import main

from app.apis_all_banks.nb_rb_api.nb_rb_pd import nb_rb_pd
from app.apis_all_banks.belarusbank_api.belka_pd import belka_bank
from app.apis_all_banks.alpha_api.aplha_pd import alpha
from app.apis_all_banks.belapb_api.belapb_pd import belapb_bank

from app.core.config import settings


logger = logging.getLogger('bank_aggregator')

broker_ = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0"

app = Celery("tasks_celery", broker=broker_, backend=broker_)


@app.task
def add_banks_to_redis():
    try:
        alpha_add_redis(URL1)
        belka_add_redis(URL2)
        nb_rb_add_redis(URL)
        belapb_add_redis(helper)
        main()
        alpha(URL1)
        belka_bank(URL2)
        nb_rb_pd(URL)
        belapb_bank(helper)

        logger.info("Redis db for banks was updated")
    except Exception as err:
        logger.error(f"something wrong in func add_banks_to_redis -- {err}")
    finally:
        logger.info("add_banks_to_redis is over")


add_banks_to_redis.delay()
