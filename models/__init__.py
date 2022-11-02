from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import BaseClass
from teams import Teams
from drivers import Drivers
from tracks import Tracks
from results import RaceResults


# dialect+driver://username:password@host:port/database
db = create_engine("postgresql+psycopg2://postgres:testpassword@localhost:5439/postgres")  

Session = sessionmaker(db)
session = Session()

BaseClass.metadata.create_all(db, checkfirst=True)
