from sqlalchemy import String, Integer, Column, Float, Date
from src.models.base import BaseClass


class Tracks(BaseClass):

    _id = Column(Integer, primary_key=True, index=True)
    
    round = Column(Integer, nullable=False, unique=True)
    country = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    circuit_name = Column(String(50), nullable=False)
    gp_name = Column(String(50), nullable=False, unique=False)
    race_date = Column(String(50), nullable=False, unique=False)
    first_gp = Column(Integer, nullable=False)
    number_of_laps = Column(Integer, nullable=False)
    circuit_length_km = Column(Float, nullable=False)
    race_distance_km = Column(Float, nullable=False)
    lap_record = Column(String(50), nullable=False)
    record_owner = Column(String(50), nullable=False)
    record_year = Column(Integer, nullable=False)
    turns = Column(Integer, nullable=False)
    drs_zones = Column(Integer, nullable=False)
