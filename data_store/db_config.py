from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from logger_conf import logger

DATABASE_URL = 'sqlite:///./addresses.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database error: {e}", exc_info=True)
        raise
    finally:
        db.close()


