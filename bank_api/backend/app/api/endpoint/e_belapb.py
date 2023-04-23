from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import logging

from app.crud.belapb import del_belapb_by_id, get_belapb_by_id
from app.schemas.belapb import BelapbModel
from app.db.session import get_db

from app.apis_all_banks.belapb_api.belapb_redis import belapb_get_from_redis

belapb_route = APIRouter()
logger = logging.getLogger('bank_aggregator')


@belapb_route.get("/get_belapb_by_id/", response_model=BelapbModel, status_code=200)
def get_belapb_id(belapb_id: int, db: Session = Depends(get_db)):
    try:
        if db_belapb := get_belapb_by_id(db, belapb_id):
            logger.info(f"Found belapb with {belapb_id}")
            return db_belapb
    except HTTPException as err:
        logger.error(f"In func get_belapb_id have an error {err}")
    except Exception as err_:
        logger.error(err_)


@belapb_route.get("/get_belapb_from_redis/", response_model=str, status_code=200)
def get_belapb_redis():
    try:
        return belapb_get_from_redis()
    except HTTPException as err:
        logger.error(f"In func get_nb_rb_redis have an error {err}")
    except Exception as err_:
        logger.error(err_)


@belapb_route.delete("/delete_belapb_by_id/", response_model=BelapbModel, status_code=200)
def del_belapb_id(belapb_id: int, db: Session = Depends(get_db)):
    try:
        if db_belapb := del_belapb_by_id(db, belapb_id):
            logger.info(f"Found belapb with {belapb_id}")
            return db_belapb
    except HTTPException as err:
        logger.error(f"In func del_belapb_id have an error {err}")
    except Exception as err_:
        logger.error(err_)


