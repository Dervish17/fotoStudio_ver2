from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATA_BASE_URL

Base = declarative_base()

_engine = create_engine(DATA_BASE_URL, echo=True)

SessionLocal = sessionmaker(bind=_engine)


def init_db():
    Base.metadata.create_all(bind=_engine)