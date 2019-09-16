import pandas as pd
import numpy as np

pl1 = pd.read_csv('csv.files/proleague.csv')
col = pl1.columns

def varlist(dataset):
    variables = dataset.columns
    datatypes = dataset.dtypes
    combo = list(zip(variables, datatypes))
    for x in combo:
        print('{}\n'.format(x))

def rateplayer(dataset, playername, variable_array=['k/d'], respawn=True):

    # ensuring player names in the data and arguments are consistent.
    playername = playername.lower()
    dataset['player'] = [x.lower() for x in dataset['player']]

    # subsetting by respawn argument
    if respawn == True:
        data = dataset[dataset['mode'] != "Search & Destroy"]
    elif respawn == False:
        data = dataset[dataset['mode'] == "Search & Destroy"]
    elif respawn == 'all' or 'All':
        data = dataset    
    else:
        raise Exception('Error: for respawn argument use either: True, False, or "all".')

    # get the averages for each column for all players     
    variable_array = ['player'] + variable_array
    data = dataset[variable_array]
    data_mu = data.groupby('player').mean()

    # get the average of each column for specified player
    player_mu = data_mu[data_mu.index == playername]
    
    # storing data points in arrays for each
    total_means = []
    player_means = []
    [total_means.append(data_mu[x].mean()) for x in data_mu.columns]
    [player_means.append(player_mu[x].mean()) for x in player_mu.columns]

    # creating the rating with the two arrays
    rating = [x - y for x, y in zip(player_means, total_means)]
    print(sum(rating), data_mu.index == 'crimsix')

rateplayer(pl1, 'crimsix')


# creating a function to generate ratings for every player at once
def generate_ratings(dataset, playername, variable_array=['k/d'], respawn=True):
    # subsetting by respawn argument
    if respawn == True:
        data = dataset[dataset['mode'] != "Search & Destroy"]
    elif respawn == False:
        data = dataset[dataset['mode'] == "Search & Destroy"]
    elif respawn == 'all' or 'All':
        data = dataset    
    else:
        raise Exception('Error: for respawn argument use either: True, False, or "all".')
       