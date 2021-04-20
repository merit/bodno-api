import os

import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_USER = settings.DATABASE_USER
DATABASE_PASSWORD = settings.DATABASE_PASSWORD
DATABASE_HOST = settings.DATABASE_HOST
DATABASE = settings.DATABASE

SQLALCHEMY_DATABASE_URL=f"mysql://{DATABASE_USER}:{str(DATABASE_PASSWORD)}@{DATABASE_HOST}/{DATABASE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_recycle=3600
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
