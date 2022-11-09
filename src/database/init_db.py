from src.database.session import SessionLocal, engine
from src.models.base import BaseClass


session = SessionLocal()
BaseClass.metadata.create_all(engine, checkfirst=True)
