from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DB_URL = 'postgresql+asyncpg://postgres:fmjuORlHSElUzEMYRjdGATPKefGzXbYN@autorack.proxy.rlwy.net:16078/railway'

# engine = create_engine('postgresql://postgres:fmjuORlHSElUzEMYRjdGATPKefGzXbYN@autorack.proxy.rlwy.net:16078/railway',
#                        echo=True,
#                        future=True)

engine = create_async_engine(DB_URL, echo=True, future=True)

# SessionLocal = sessionmaker(engine, expire_on_commit=False)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncSessionLocal:
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


class Base(DeclarativeBase):
    pass
