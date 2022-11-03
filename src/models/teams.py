from sqlalchemy import String, Integer, Column
from src.models.base import BaseClass


class Teams(BaseClass):

    _id = Column(Integer, primary_key=True, index=True)

    name = Column(String(50), nullable=False, unique=False)
