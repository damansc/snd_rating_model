import pandas as pd
import os

def parse_dir(files_dir):
    GAMES = ['IW', 'WW2', 'Bo4', 'MW']
    files_dir = files_dir
    file_list = os.listdir(files_dir)
    events = [file_list[x][16:-4] for x, y in enumerate(file_list)]
    dates = pd.to_datetime([file_list[x][5:15] for x, y in enumerate(file_list)])
    stats = [pd.read_csv('data\{}'.format(file_list[x])) for x, y in enumerate(file_list)]
    game = list()
    for x in dates:
        if x <= pd.to_datetime('2017-08-13'):
            game.append(GAMES[0])
        elif x <= pd.to_datetime('2018-08-19'):
            game.append(GAMES[1])
        elif x <= pd.to_datetime('2019-08-18'):
            game.append(GAMES[2])
        else:
            game.append(GAMES[3])
    glance = pd.DataFrame({
                            'event' : events,
                            'game' : game, 
                            'date' : dates,
                            'path' : file_list
                            })
    metadata = dict(zip(events, stats))
    return glance, metadata   


###################### NEW CODE ABOVE
class Event_Parser:


    GAMES = ['IW', 'WW2', 'Bo4', 'MW']

    def __init__(self, files_dir):
        GAMES = ['IW', 'WW2', 'Bo4', 'MW']
        self.files_dir = files_dir
        self.file_list = os.listdir(files_dir)
        self.events = [self.file_list[x][16:-4] for x, y in enumerate(self.file_list)]
        self.dates = pd.to_datetime([self.file_list[x][5:15] for x, y in enumerate(self.file_list)])
        self.stats = [pd.read_csv('data\{}'.format(self.file_list[x])) for x, y in enumerate(self.file_list)]
        self.game = list()
        for x in self.dates:
            if x <= pd.to_datetime('2017-08-13'):
                self.game.append(GAMES[0])
            elif x <= pd.to_datetime('2018-08-19'):
                self.game.append(GAMES[1])
            elif x <= pd.to_datetime('2019-08-18'):
                self.game.append(GAMES[2])
            else:
                self.game.append(GAMES[3])
        self.glance = pd.DataFrame({
                                  'event' : self.events,
                                  'game' : self.game, 
                                  'date' : self.dates,
                                  'path' : self.file_list
                                  })
        self.meta = dict(zip(self.events, self.stats))                                  

    
    def filter_meta(self, game_title=None, variables=None):
        BASE_VARS = ['match id', 'mode', 'map', 'team', 'player', 'win?']
        if game_title:
            ind = list(self.glance[self.glance['game'] == game_title].index)
            data = self.stats[ind[0]:ind[-1]+1]
            events = self.events[ind[0]:ind[-1]+1]
            self.filtered = dict(zip(events, data))
            print(self.filtered.keys())
        else:
            self.filtered = self.meta
        if variables:
            for x in self.filtered:
                self.filtered = self.filtered[x][BASE_VARS + variables]
        return self.filtered
        

test = Event_Parser('data/')
IW = test.filter_meta('Bo4', ['k/d'])
IW