from sqlalchemy import create_engine
from app.core.config import settings
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


# sync

# SQLALCHEMY_DATABASE_URL_FOR_PD = f'postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@' \
#                           f'{settings.DB_HOST}:{settings.DB_PORT}/{settings.POSTGRES_DB}'
SQLALCHEMY_DATABASE_URL_FOR_PD = f'postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@' \
                          f'db_app_postgres:{settings.DB_PORT}/{settings.POSTGRES_DB}'

engine_pd = create_engine(SQLALCHEMY_DATABASE_URL_FOR_PD)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_pd)


# acync
# SQLALCHEMY_DATABASE_URL = f'postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@' \
#                           f'{settings.DB_HOST}:{settings.DB_PORT}/{settings.POSTGRES_DB}'

SQLALCHEMY_DATABASE_URL = f'postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@' \
                          f'db_app_postgres:{settings.DB_PORT}/{settings.POSTGRES_DB}'

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
