from sqlalchemy import String, Integer, Column, ForeignKey
from base import BaseClass


class RaceResults(BaseClass):
    _id = Column(Integer, primary_key=True, index=True)
    _track_id = Column(Integer, ForeignKey("tracks._id"))
    position = Column(Integer, nullable=False, unique=False)
    no = Column(Integer, nullable=False, unique=False)
    _driver_id = Column(Integer, ForeignKey("drivers._id"))
    _team_id = Column(Integer, ForeignKey("teams._id"))
    starting_grid = Column(Integer, nullable=False, unique=False)
    laps = Column(Integer, nullable=False, unique=False)
    total_time_gap_retirement = Column(String(50), nullable=False, unique=False)
    points = Column(Integer, nullable=False, unique=False)
    fastest_lap = Column(String(50), nullable=False, unique=False)
