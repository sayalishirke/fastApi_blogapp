from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'mysql+mysqlconnector://root:password@localhost:3306/blogmodified'

engine = create_engine(SQLALCHAMY_DATABASE_URL, encoding='latin1', echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db    # return generator object
    finally:
        db.close()