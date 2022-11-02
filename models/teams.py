from lib2to3.pytree import Base
from sqlalchemy import String, Integer, Column
from base import BaseClass


class Teams(BaseClass):
    _id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=False)
