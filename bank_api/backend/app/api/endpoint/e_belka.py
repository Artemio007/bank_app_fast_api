from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import logging

from app.crud.belarusbank import del_belka_by_id, get_belka_by_id
from app.schemas.belarusbank import BelkaModel
from app.db.session import get_db

from app.apis_all_banks.belarusbank_api.belka_redis import belarusbank_get_from_redis

from app.apis_all_banks.belarusbank_api.belka_pd import belka_bank, URL2


belka_route = APIRouter()
logger = logging.getLogger('bank_aggregator')


@belka_route.get("/get_belka_by_id/", response_model=BelkaModel, status_code=200)
def get_belka_id(belka_id, db: Session = Depends(get_db)):
    try:
        if db_belka := get_belka_by_id(db, belka_id):
            logger.info(f"Found belka with {belka_id}")
            return db_belka
    except HTTPException as err:
        logger.error(f"In func get_belka_id have an error {err}")
    except Exception as err_:
        logger.error(err_)


@belka_route.get("/get_belka_from_redis/", response_model=str, status_code=200)
def get_belka_redis():
    try:
        return belarusbank_get_from_redis()
    except HTTPException as err:
        logger.error(f"Func get_belka_redis have an error {err}")
    except Exception as err_:
        logger.error(err_)


@belka_route.delete("/delete_belka_by_id/", response_model=BelkaModel, status_code=200)
def del_belka_id(belka_id, db: Session = Depends(get_db)):
    try:
        if db_belka := del_belka_by_id(db, belka_id):
            logger.info(f"Found belka with {belka_id}")
            return db_belka
    except HTTPException as err:
        logger.error(f"In func del_belka_id have an error {err}")
    except Exception as err_:
        logger.error(err_)


@belka_route.get("/get_belka_from_BANK_API/", status_code=200)
def get_belka__bank_api():
    try:
        return belka_bank(URL2)
    except HTTPException as err:
        logger.error(f"Func get_belka__bank_api have an error {err}")
    except Exception as err_:
        logger.error(err_)

