import os
import pandas as pd


DATA_FILES_DIRECTORY = "./data/"


def get_graph_data():
    dataframe = pd.read_csv(os.path.join(DATA_FILES_DIRECTORY, 'formula1_2020season_raceResults.csv'))

    winners = dataframe[dataframe['Position'] == '1']
    podium_finish = dataframe[dataframe['Position'].isin(('1', '2', '3'))]
    return (
        dataframe.groupby('Team')['Points'].sum().sort_values(ascending=False).reset_index(),
        dataframe.groupby('Driver')['Points'].sum().sort_values(ascending=False).reset_index(),
        winners['Driver'].value_counts().reset_index().rename(columns={"index": "Driver", "Driver": "Win Count"}),
        podium_finish['Driver'].value_counts().reset_index().rename(columns={"index": "Driver", "Driver": "Podium Count"})
    )