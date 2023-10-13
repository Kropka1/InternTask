from app.config.settings import settings
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(settings.db_url)


async def get_session() -> AsyncSession:
    async_session = async_sessionmaker(engine)
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
