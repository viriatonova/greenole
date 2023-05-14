from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from api.settings import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_USER

# Api database 
DB = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
ENGINE = create_engine(DB)
SESSION = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
BASE = declarative_base()

# Tests database
DB_TESTS = "sqlite:///./tests/sqlite.db"
ENGINE_TESTS = create_engine(DB_TESTS, connect_args={"check_same_thread": False})
SESSION_TESTS = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE_TESTS)
BASE_TESTS = declarative_base()


def get_db():
    db = SESSION()
    try:
        yield db
    finally:
        db.close()

def tests_db():
    db = SESSION_TESTS()
    try:
        yield db
    finally:
        db.close()
