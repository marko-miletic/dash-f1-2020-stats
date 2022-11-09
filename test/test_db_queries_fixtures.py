import pytest

from src.models.drivers import Drivers
from src.models.tracks import Tracks
from src.models.results import RaceResults


@pytest.fixture
def drivers_fixture():
    drivers_unit = Drivers(
        _id=1000,

        name='test',
        abbreviation='test',
        number='test',
        country='test',
        podiums='test',
        points=0,
        grands_prix_entered='test',
        world_championships='test',
        highest_race_finish='test',
        highest_grid_position='test',
        date_of_birth='test',
        place_of_birth='test',

        _team_id=0
    )
    return drivers_unit


@pytest.fixture
def calendars_fixture():
    calendars_unit = Tracks(
        _id=1000,

        round=0,
        country='test',
        city='test',
        circuit_name='test',
        gp_name='test',
        race_date='test',
        first_gp=0,
        number_of_laps=0,
        circuit_length_km=0,
        race_distance_km=0,
        lap_record='test',
        record_owner='test',
        record_year=0,
        turns=0,
        drs_zones=0
    )
    return calendars_unit


@pytest.fixture
def race_results_fixture():
    race_results_unit = RaceResults(
        _id=1000,

        position='test',
        no=0,
        starting_grid=0,
        laps=0,
        total_time_gap_retirement='test',
        points=0,
        fastest_lap=True,

        _track_id=0,
        _driver_id=0,
        _team_id=0
    )
    return race_results_unit
