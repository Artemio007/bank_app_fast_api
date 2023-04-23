import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.user import get_user_by_id, get_user_list
from app.schemas.user import UserModel
from app.db.session import get_db


user_route = APIRouter()
logger = logging.getLogger("bookshelf")


@user_route.get("/{user_id}", response_model=UserModel, status_code=200)
def get_user(user_id: int, db: Session = Depends(get_db)):
    if user := get_user_by_id(db, user_id):
        logger.info(f"User with id {user_id} was returned")
        return user
    else:
        logger.error(f"User with id {user_id} doesn't exist")
        return HTTPException(status_code=404, detail=f"User with id {user_id} doesn't exist")


@user_route.get("/users_all/", response_model=list[UserModel], status_code=200)
def get_users(db: Session = Depends(get_db)):
    logger.info(f"list was returned")
    return get_user_list(db)
