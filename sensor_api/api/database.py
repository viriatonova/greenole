from api.settings import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_USER
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Api database
DB = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
ENGINE = create_engine(DB)
SESSION = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
BASE = declarative_base()


def get_db():
    db = SESSION()
    try:
        yield db
    finally:
        db.close()
