from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import get_db_connection_url

engine = create_engine(get_db_connection_url(), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
