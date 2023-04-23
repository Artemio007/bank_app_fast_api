from app.db.db_setup import SessionLocal

from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_setup import async_session_maker


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
