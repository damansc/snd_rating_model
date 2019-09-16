import pandas as pd 
import os

"""
Reads in the specified variables from all csv files, identifies the game + event, 
and concatenates to one single tall dataframe.
"""

SND = ['match id', 'series id', 'duration (s)', 'mode', 'map', 'team', 'player', \
        'win?', 'score', 'kills', 'deaths', '+/-', 'k/d', 'kills per 10min', \
        'deaths per 10min', 'assists', 'team kills', \
        'hits', 'shots', 'accuracy (%)',   \
        'snd rounds', 'snd firstbloods', \
        'bomb pickups', 'bomb plants', 'bomb defuses', \
        'bomb sneak defuses', "2-piece","3-piece","4-piece", \
        "4-streak","5-streak","6-streak","7-streak","8+-streak",]

def read_filter(path='data/', variables=SND):
    df = pd.DataFrame(columns=variables + ['game', 'event'])
    file_list = os.listdir(path)
    for x in file_list:
        games = ['IW', 'WW2', 'Bo4', 'MW']
        temp1 = pd.read_csv('data/{}'.format(x))
        temp2 = temp1[variables]
        date = pd.to_datetime(x[5:15])
        if date <= pd.to_datetime('2017-08-13'):
            temp2['game'] = games[0]
        elif date <= pd.to_datetime('2018-08-19'):
            temp2['game'] = games[1]
        elif date <= pd.to_datetime('2019-08-18'):
            temp2['game'] = games[2]
        else:
            temp2['game'] = games[3]
        event = x[16:-4]
        temp2['event'] = event
        df = df.append(temp2, ignore_index = True)
    return df

data = read_filter()

test = read_filter(variables=['player', 'win?'])

test['win?'] = test['win?'].map({'W' : 1, 'L' : 0})
wins = test[test['game'] == 'Bo4'].groupby('player')['win?'].sum().sort_values(ascending=False)
total = test[test['game'] == 'Bo4'].groupby('player')['win?'].count()
ratio = wins/total
round(ratio, 2).sort_values(ascending=False).head(30)
