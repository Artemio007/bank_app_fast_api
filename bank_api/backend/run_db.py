import logging.config

from app.core.config import LOGGING_CONFIG
from app.db.db_setup import SessionLocal
from app.db.init_db import init_db
from app.db.db_setup import async_session_maker

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('bank_aggregator')


def init():
    db = SessionLocal()
    adb = async_session_maker()
    init_db(db, adb)


def main():
    logger.info('Run initialization')
    try:
        init()
    except Exception as error:
        logger.error(f"An error during db initialization {error}")
    else:
        logger.info('End initialization')



