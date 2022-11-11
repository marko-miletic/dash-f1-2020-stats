from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import assemble_db_connection

engine = create_engine(assemble_db_connection(), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
