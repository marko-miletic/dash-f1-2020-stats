from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, PrimaryKeyConstraint, String, Date, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



db_string = "postgresql+psycopg2://postgres:testpassword@localhost:5439/postgres"
db = create_engine(db_string)  
base = declarative_base()

class Team(base):
    __tablename__ = 'teams'
    _id = Column(Integer, primary_key= True)
    name = Column(String)

class Driver(base):
    __tablename__ = 'drivers'
    _id = Column(Integer, primary_key= True)
    _team_id = Column(Integer, ForeignKey("teams._id"))
    abbreviation = Column(String)
    number = Column(Integer)
    country = Column(String)
    podiums = Column(String)
    points = Column(Integer)
    grands_prix_entered = Column(String)
    world_championships = Column(String)
    highest_race_finish = Column(String)
    highest_grid_position = Column(String)
    date_of_birth = Column(Date)
    place_of_birth = Column(String)

class Track(base):
    __tablename__ = 'tracks'
    _id = Column(Integer, primary_key= True)
    round = Column(Integer)
    country = Column(String)
    city = Column(String)
    circuit_name = Column(String)
    gp_name = Column(String)
    race_date = Column(Date)
    first_gp = Column(Integer)
    number_of_laps = Column(Integer)
    circuit_length_km = Column(Float)
    race_distance_km = Column(Float)
    lap_record = Column(String)
    record_owner = Column(String)
    record_year = Column(Integer)
    turns = Column(Integer)
    drs_zones = Column(Integer)

class RaceResults(base):
    __tablename__ = 'race_results'
    _id = Column(Integer, primary_key= True)
    _track_id = Column(Integer, ForeignKey("tracks._id"))
    position = Column(Integer)
    no = Column(Integer)
    _driver_id = Column(Integer, ForeignKey("drivers._id"))
    _team_id = Column(Integer, ForeignKey("teams._id"))
    starting_grid = Column(Integer)
    laps = Column(Integer)
    total_time_gap_retirement = Column(String)
    points = Column(Integer)
    fastest_lap = Column(String)

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)

