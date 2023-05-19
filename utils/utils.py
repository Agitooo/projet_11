import json


def loadClubs():
    with open('../clubs.json') as clubs:
        clubs_list = json.load(clubs)['clubs']
        return clubs_list


def loadCompetitions():
    with open('../competitions.json') as comps:
        competitions_list = json.load(comps)['competitions']
        return competitions_list
