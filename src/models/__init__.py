from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models.base import BaseClass
from src.models.teams import Teams
from src.models.drivers import Drivers
from src.models.tracks import Tracks
from src.models.results import RaceResults


# dialect+driver://username:password@host:port/database
#db = create_engine("postgresql+psycopg2://postgres:testpassword@localhost:5439/postgres")  

#Session = sessionmaker(db)
#session = Session()

#BaseClass.metadata.create_all(db, checkfirst=True)
