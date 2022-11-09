import pandas as pd

from src.database.session import SessionLocal
from src.database.session import engine

from src.models.drivers import Drivers
from src.models.tracks import Tracks
from src.models.results import RaceResults

from src.database.db_queries import get_drivers_query
from src.database.db_queries import get_calendar_query
from src.database.db_queries import get_race_results_query

from test_db_queries_fixtures import drivers_fixture
from test_db_queries_fixtures import calendars_fixture
from test_db_queries_fixtures import race_results_fixture


def test_get_drivers_query(drivers_fixture):
    session = SessionLocal()

    session.add(drivers_fixture)
    session.commit()

    query = get_drivers_query()
    test_df = pd.read_sql_query(query, engine)

    assert len(test_df[test_df['Driver'] == 'test']) >= 1


def test_get_calendar_query(calendars_fixture):
    session = SessionLocal()

    session.add(calendars_fixture)
    session.commit()

    query = get_calendar_query()
    test_df = pd.read_sql_query(query, engine)
    assert len(test_df[test_df['Circuit Name'] == 'test']) >= 1


def test_get_race_results_query(race_results_fixture):
    session = SessionLocal()

    session.add(race_results_fixture)
    session.commit()

    query = get_race_results_query()
    test_df = pd.read_sql_query(query, engine)
    assert len(test_df[test_df['Position'] == 'test']) >= 1
