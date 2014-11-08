#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.player import Player

class Game(object):
    '''
    Game
    '''
    def __init__(self,mode=None):
        self.mode = mode
        self.home_team = ''
        self.away_team = ''
        if mode == 'test':
            self.init_test_game()


    def init_test_game(self):
        self.home_team = Team('home','test')
        self.away_team = Team('away','test')




class Team(object):
    '''
    Team
    '''
    def __init__(self,side,mode=None):
        self.side = side
        self.player_list = []
        self.strategy = ''

        self.forward = []
        self.mid = []
        self.defence = []

        if mode == 'test':
            self.player_list = self.init_test_players()


    def init_test_players(self):
        players = []
        for i in range(0,5):
            players.append(Player(mode='test'))
        return players





if __name__ == '__main__':
    a = Game(mode='test')





