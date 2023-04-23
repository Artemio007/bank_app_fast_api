import logging
from typing import List

import bcrypt
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.exceptions import FastAPIUsersException
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.db.session import get_async_session


logger = logging.getLogger('bank_aggregator')


async def create_init_user(db: AsyncSession, user: User) -> User:
    try:
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        db_user = User(
            user_name=user.user_name,
            email=user.email,
            hashed_password=str(hashed_password),
        )
        db.add(db_user)
        await db.commit()
        logger.info(f'Created user db {db_user}')
        return db_user
    except FastAPIUsersException as err:
        logger.info(f"Have an error in crud/create_init_user - {err}")
    except Exception as err:
        logger.info(f"Have an error in crud/create_init_user - {err}")


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_by_id(db: AsyncSession, id_: int) -> User:
    try:
        return db.query(User).filter(User.id == id_).first()
    except Exception as err:
        logger.error(f"Func crud/get_user_by_id have an error: {err}")


async def get_user_list(db: AsyncSession) -> List[User]:
    try:
        return db.query(User).all()
    except Exception as err:
        logger.error(f"Have an error in crud/get_users_list {err}")


