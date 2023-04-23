import asyncio
import logging

from fastapi_users.exceptions import FastAPIUsersException
from pydantic import ValidationError
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import Settings

from app.schemas.user import UserCreate
from app.schemas.alphabank import AlphaCreateModel
from app.schemas.belarusbank import BelkaCreateModel
from app.schemas.nb_rb import NbRbCreateModel
from app.schemas.belapb import BelapbCreateModel

from app.crud.user import create_init_user
from app.crud.alphabank import create_alpha_bank
from app.crud.belarusbank import create_belka_bank
from app.crud.belapb import create_belapb_bank
from app.crud.nb_rb import create_nb_rb_bank

settings = Settings()
logger = logging.getLogger('bank_aggregator')


def init_db(db: Session, adb: AsyncSession):
    # create_alpha(db)
    # create_belapb(db)
    # create_nb_rb(db)
    # create_belka(db)
    asyncio.run(create_user(adb))


async def create_user(db: AsyncSession) -> None:
    user = settings.INIT_USER
    try:
        db_user = UserCreate(
            user_name=user['user_name'],
            email=user['email'],
            password=user['password']
        )
    except ValidationError as err:
        logger.error(f"You have some err in func 'create_user': {err}")
    except FastAPIUsersException as err:
        logger.info(f"have an error in init db create_user {err}")
    except Exception as err:
        logger.info(f"have an error in init db create_user {err}")
    else:
        async with db.begin():
            await create_init_user(db, db_user)


def create_alpha(db: Session):
    alpha = settings.INIT_ALPHA_BELKA
    try:
        db_alpha = AlphaCreateModel(
            sell_currency=alpha['sell_currency'],
            buy_currency=alpha['buy_currency'],
            bank_sell=alpha['bank_sell'],
            bank_buy=alpha['bank_buy']
        )
    except TypeError as t_err:
        logger.info(f"Typeerror in func 'create_alpha': {t_err}")
    except Exception as err:
        logger.info(f"Some error in func 'create_alpha': {err}")
    else:
        create_alpha_bank(db, db_alpha)


def create_belka(db: Session):
    belka = settings.INIT_ALPHA_BELKA
    try:
        db_belka = BelkaCreateModel(
            sell_currency=belka['sell_currency'],
            buy_currency=belka['buy_currency'],
            bank_sell=belka['bank_sell'],
            bank_buy=belka['bank_buy'],
        )
    except TypeError as t_err:
        logger.info(f"Typeerror in func 'create_belka': {t_err}")
    except Exception as err:
        logger.info(f"Some error in func 'create_belka': {err}")
    else:
        create_belka_bank(db, db_belka)


def create_belapb(db: Session):
    belapb = settings.INIT_NB_BELAPB
    try:
        db_belapb = BelapbCreateModel(
            sell_currency=belapb['sell_currency'],
            buy_currency=belapb['buy_currency'],
            convert=belapb['convert']
        )
    except TypeError as t_err:
        logger.info(f"Typeerror in func 'create_belapb': {t_err}")
    except Exception as err:
        logger.info(f"Some error in func 'create_belapb': {err}")
    else:
        create_belapb_bank(db, db_belapb)


def create_nb_rb(db: Session):
    nb_rb = settings.INIT_NB_BELAPB
    try:
        db_nb_rb = NbRbCreateModel(
            sell_currency=nb_rb['sell_currency'],
            buy_currency=nb_rb['buy_currency'],
            convert=nb_rb['convert']
        )
    except TypeError as t_err:
        logger.info(f"Typeerror in func 'create_nb_rb': {t_err}")
    except Exception as err:
        logger.info(f"Some error in func 'create_nb_rb': {err}")
    else:
        create_nb_rb_bank(db, db_nb_rb)
