from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import logging

from app.crud.alphabank import del_alpha_by_id, get_alpha_by_id
from app.schemas.alphabank import AlphaModel
from app.db.session import get_db

from app.apis_all_banks.alpha_api.alpha_redis import alpha_get_from_redis

alpha_route = APIRouter()
logger = logging.getLogger('bank_aggregator')


@alpha_route.get("/get_alpha_by_id/", response_model=AlphaModel, status_code=200)
def get_alpha_id(alpha_id: int, db: Session = Depends(get_db)):
    try:
        if db_alpha := get_alpha_by_id(db, alpha_id):
            logger.info(f"Found alpha with {alpha_id}")
            return db_alpha
    except HTTPException as err:
        logger.error(f"In func get_alpha_id have an error {err}")
    except Exception as err_:
        logger.error(err_)


@alpha_route.get("/get_alpha_from_redis/", response_model=str, status_code=200)
def get_alpha_redis():
    try:
        return alpha_get_from_redis()
    except HTTPException as err:
        logger.error(f"Func get_alpha_redis have an error {err}")
    except Exception as err_:
        logger.error(err_)


@alpha_route.delete("/delete_alpha_by_id/", response_model=AlphaModel, status_code=200)
def del_alpha_id(alpha_id: int, db: Session = Depends(get_db)):
    try:
        if db_alpha := del_alpha_by_id(db, alpha_id):
            logger.info(f"Found alpha with {alpha_id}")
            return db_alpha
    except HTTPException as err:
        logger.error(f"In func del_alpha_id have an error {err}")
    except Exception as err_:
        logger.error(err_)


