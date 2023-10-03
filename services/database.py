from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHAMY_DATABASE_URL = 'mysql+pymysql://admin:SkoogEarth123!@104.199.205.12:3306/public'
engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
