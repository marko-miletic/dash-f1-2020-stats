import pandas as pd

from src.database.session import engine
from src.database.db_queries import get_race_results_query


def get_graph_data():
    dataframe = pd.read_sql_query(get_race_results_query(), engine)

    winners = dataframe[dataframe['Position'] == '1']
    podium_finish = dataframe[dataframe['Position'].isin(('1', '2', '3'))]
    return (
        dataframe.groupby('Team')['Points'].sum().sort_values(ascending=False).reset_index(),
        dataframe.groupby('Driver')['Points'].sum().sort_values(ascending=False).reset_index(),
        winners['Driver'].value_counts().reset_index().rename(columns={"index": "Driver", "Driver": "Win_Count"}),
        podium_finish['Driver'].value_counts().reset_index().rename(columns={"index": "Driver", "Driver": "Podium_Count"})
    )
