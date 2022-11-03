from sqlalchemy import String, Integer, Column, ForeignKey, Date
from base import BaseClass


class Drivers(BaseClass):
    
    _id = Column(Integer, primary_key=True, index=True)

    abbreviation = Column(String(50), nullable=False, unique=True)
    number = Column(Integer, nullable=False, unique=True)
    country = Column(String(50), nullable=False, unique=False)

    podiums = Column(String(50), nullable=False, unique=False)
    points = Column(Integer, nullable=False, unique=False)
    grands_prix_entered = Column(String(50), unique=False)
    world_championships = Column(String(50), unique=False)
    highest_race_finish = Column(String(50), unique=False)
    highest_grid_position = Column(String(50), unique=False)
    date_of_birth = Column(Date, unique=False)
    place_of_birth = Column(String(50), unique=False)

    _team_id = Column(Integer, ForeignKey("teams._id"))
