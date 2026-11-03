from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

database_url = os.getenv("DATABASE_URL","mysql+pymysql://root:Root310797@localhost:3306/contactManagerDB")
engine = create_engine(database_url)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_database():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()