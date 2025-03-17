from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator, Annotated
from app.core.config import settings
from fastapi import Depends

class Base(AsyncAttrs, DeclarativeBase):
    pass

engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=True)
Session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with Session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_db)]