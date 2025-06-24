from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine


SQLITE_URL = "sqlite:///./test.db"


engine = create_engine(SQLITE_URL, echo=True)


SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass
