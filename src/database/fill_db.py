import os
import pandas as pd

from src.database.session import SessionLocal
from src.models.teams import Teams
from src.models.drivers import Drivers
from src.models.tracks import Tracks
from src.models.results import RaceResults

from src.src_path_structure import DATA_FILES_PATH


def fill_database() -> None:

    session = SessionLocal()

    teams_key_relation = dict()
    drivers_key_relation = dict()
    tracks_key_relation = dict()

    drivers_dataframe = pd.read_csv(os.path.join(DATA_FILES_PATH, 'formula1_2020season_drivers.csv'))

    teams_set = set(drivers_dataframe['Team'])

    for key, team_name in enumerate(teams_set):
        session.add(Teams(
            _id=key,

            name=team_name)
        )
        teams_key_relation[team_name] = key
    
    session.commit()


    for index, row in drivers_dataframe.iterrows():
        session.add(Drivers(
            _id=index,

            name=row['Driver'],
            abbreviation=row['Abbreviation'],
            number=row['Number'],
            country=row['Country'],
            podiums=row['Podiums'],
            points=int(row['Points']),
            grands_prix_entered=row['Grands Prix Entered'],
            world_championships=row['World Championships'],
            highest_race_finish=row['Highest Race Finish'],
            highest_grid_position=row['Highest Grid Position'],
            date_of_birth=row['Date of Birth'],
            place_of_birth=row['Place of Birth'],

            _team_id=teams_key_relation[row['Team']]
        ))
        drivers_key_relation[row['Driver']] = index

    session.commit()


    tracks_dataframe = pd.read_csv(os.path.join(DATA_FILES_PATH, 'formula1_2020season_calendar.csv'))

    for index, row in tracks_dataframe.iterrows():
        session.add(Tracks(
            _id=index,

            round=int(row['Round']),
            country=row['Country'],
            city=row['City'],
            circuit_name=row['Circuit Name'],
            gp_name=row['GP Name'],
            race_date=row['Race Date'],
            first_gp=int(row['First GP']),
            number_of_laps=int(row['Number of Laps']),
            circuit_length_km=float(row['Circuit Length(km)']),
            race_distance_km=float(row['Race Distance(km)']),
            lap_record=row['Lap Record'],
            record_owner=row['Record Owner'],
            record_year=int(row['Record Year']),
            turns=int(row['Turns']),
            drs_zones=int(row['DRS Zones'])
        ))
        tracks_key_relation[row['GP Name']] = index

    results_dataframe = pd.read_csv(os.path.join(DATA_FILES_PATH, 'formula1_2020season_raceResults.csv'))

    session.commit()


    fastest_lap_switch = {
        'Yes': True,
        'No': False
    }

    results_dataframe = results_dataframe.replace('Racing Point BWT Mercedes', 'Racing Point')
    results_dataframe = results_dataframe.replace('AlphaTauri Honda', 'AlphaTauri')
    results_dataframe = results_dataframe.replace('Alfa Romeo Racing Ferrari', 'Alfa Romeo')
    results_dataframe = results_dataframe.replace('Williams Mercedes', 'Williams')
    results_dataframe = results_dataframe.replace('Red Bull Racing Honda', 'Red Bull Racing')
    results_dataframe = results_dataframe.replace('Haas Ferrari', 'Haas')

    for index, row in results_dataframe.iterrows():
        session.add(RaceResults(
            _id=index,

            position=row['Position'],
            no=int(row['No']),
            starting_grid=int(row['Starting Grid']),
            laps=int(row['Laps']),
            total_time_gap_retirement=row['Total Time/Gap/Retirement'],
            points=int(row['Points']),
            fastest_lap=fastest_lap_switch[row['Fastest Lap']],

            _track_id=tracks_key_relation[row['Track']],
            _driver_id=drivers_key_relation[row['Driver']],
            _team_id=teams_key_relation[row['Team']]
        ))

    session.commit()
