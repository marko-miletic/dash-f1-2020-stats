from src.database.session import SessionLocal
from src.models.drivers import Drivers
from src.models.teams import Teams
from src.models.tracks import Tracks
from src.models.results import RaceResults

session = SessionLocal()

def get_drivers_query():
    drivers_query = session.query(
        Drivers.name.label('Driver'),
        Drivers.abbreviation.label('Abbreviation'),
        Drivers.number.label('Number'),
        Teams.name.label('Team'),
        Drivers.country.label('Country'),
        Drivers.podiums.label('Podiums'),
        Drivers.points.label('Points'),
        Drivers.grands_prix_entered.label('Grands Prix Entered'),
        Drivers.world_championships.label('World Championships'),
        Drivers.highest_race_finish.label('Highest Race Finish'),
        Drivers.highest_grid_position.label('Highest Grid Position'),
        Drivers.date_of_birth.label('Date of Birth'),
        Drivers.place_of_birth.label('Place of Birth')
    ).join(Teams)
    return drivers_query.statement

def get_calendar_query():
    calendar_query = session.query(
        Tracks.round.label('Round'),
        Tracks.country.label('Country'),
        Tracks.city.label('City'),
        Tracks.circuit_name.label('Circuit Name'),
        Tracks.gp_name.label('GP Name'),
        Tracks.race_date.label('Race Date'),
        Tracks.first_gp.label('First GP'),
        Tracks.number_of_laps.label('Number of Laps'),
        Tracks.circuit_length_km.label('Circuit Length (km)'),
        Tracks.race_distance_km.label('Race Distance (km)'),
        Tracks.lap_record.label('Lap Record'),
        Tracks.record_owner.label('Record Owner'),
        Tracks.record_year.label('Record Year'),
        Tracks.turns.label('Turns'),
        Tracks.drs_zones.label('DRS Zones')
    )
    return calendar_query.statement

def get_race_results_query():
    race_results_query = session.query(
        RaceResults.position.label('Position'),
        Tracks.gp_name.label('Track'),
        Drivers.number.label('No'),
        Drivers.name.label('Driver'),
        Teams.name.label('Team'),
        RaceResults.starting_grid.label('Starting Grid'),
        RaceResults.laps.label('Laps'),
        RaceResults.total_time_gap_retirement.label('Time - Gap - Retirement'),
        RaceResults.points.label('Points'),
        RaceResults.fastest_lap.label('Fastest Lap')
    ).join(Tracks).join(Drivers).join(Teams)
    return race_results_query.statement
