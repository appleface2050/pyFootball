#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.player import Player

class Squad(object):
    '''
    Team
    '''
    def __init__(self,side,team_name,mode=None):
        self.team_name = team_name
        self.side = side
        self.player_list = []
        self.strategy = None

        self.forward = []
        self.mid = []
        self.defence = []

        if mode == 'test':
            self.player_list = self.init_test_players()
            self.init_test_squad()
            self.strategy = self.init_test_strategy()

    def init_test_players(self):
        players = []
        for i in range(0,5):
            players.append(Player(mode='test'))
        return players

    def init_test_strategy(self):
        pass

    def init_test_squad(self):
        self.forward = [self.player_list[0]]
        self.mid = self.player_list[1:3]
        self.defence = self.player_list[3:5]

    def get_strategy(self):
        return self.strategy

    def get_forward(self):
        return self.forward

    def get_mid(self):
        return self.mid

    def get_defence(self):
        return self.defence

    def __str__(self):
        return self.team_name

