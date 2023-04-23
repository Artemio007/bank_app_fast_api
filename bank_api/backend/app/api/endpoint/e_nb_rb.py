from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import logging

from app.crud.nb_rb import del_nb_rb_by_id, get_nb_rb_by_id
from app.schemas.nb_rb import NbRbModel
from app.db.session import get_db
from app.apis_all_banks.nb_rb_api.nb_rb_redis import nb_rb_get_from_redis


nb_rb_route = APIRouter()
logger = logging.getLogger('bank_aggregator')


@nb_rb_route.get("/get_nb_rb_by_id/", response_model=NbRbModel, status_code=200)
def get_nb_rb_id(nb_rb_id: int, db: Session = Depends(get_db)):
    try:
        if db_nb := get_nb_rb_by_id(db, nb_rb_id):
            logger.info(f"Found nb_rb with {nb_rb_id}")
            return db_nb
    except HTTPException as err:
        logger.error(f"In func get_nb_rb_id have an error {err}")
    except Exception as err_:
        logger.error(err_)


@nb_rb_route.get("/get_nb_rb_from_redis/", response_model=str, status_code=200)
def get_nb_rb_redis():
    try:
        return nb_rb_get_from_redis()
    except HTTPException as err:
        logger.error(f"In func get_nb_rb_redis have an error {err}")
    except Exception as err_:
        logger.error(err_)


@nb_rb_route.delete("/delete_nb_rb_by_id/", response_model=NbRbModel, status_code=200)
def del_nb_rb_id(nb_rb_id: int, db: Session = Depends(get_db)):
    try:
        if db_nb := del_nb_rb_by_id(db, nb_rb_id):
            logger.info(f"Found nb_rb with {nb_rb_id}")
            return db_nb
    except HTTPException as err:
        logger.error(f"In func del_nb_rb_id have an error {err}")
    except Exception as err_:
        logger.error(err_)


