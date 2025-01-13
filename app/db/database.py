from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine, URL

DB_URL = URL.create(
    'postgresql',
    username='postgres',
    password='fmjuORlHSElUzEMYRjdGATPKefGzXbYN',
    host='postgres.railway.internal',
    port=5432,
    database='railway',
    query={'client_encoding': 'utf8'}
)

engine = create_engine('postgresql://postgres:fmjuORlHSElUzEMYRjdGATPKefGzXbYN@autorack.proxy.rlwy.net:16078/railway', echo=True)

SessionLocal = sessionmaker(engine, expire_on_commit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass
