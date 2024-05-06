from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from ..logger_conf import logger


DATABASE_URL = 'sqlite:///./database.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database error: {e}", exc_info=True)
    finally:
        db.close()


