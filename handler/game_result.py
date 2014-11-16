#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handler.squad import Squad
from conf.game_conf import BACKFIELD_ATT,MIDFIELD_ATT,FRONTFIELD_ATT,ATT_BALL_POSITION
from data.exceptions import MatcheException
from lib.utils import multy_random_one,random_result

class GameResult(object):
    '''
    Game Result
    '''
    def __init__(self, home_team, away_team):
        self.home_team_res = TeamResult(home_team.get_team_name(),home_team.get_side(),home_team.get_player_name_list())
        self.away_team_res = TeamResult(away_team.get_team_name(),away_team.get_side(),away_team.get_player_name_list())

    def assert_side_deco(func):
        def _assert_side_deco(side):
            print side
            #assert side in ('home','away')
            return func(side)
        return _assert_side_deco

    @assert_side_deco
    def acc_score(self, side):
        '''
        side: home, away
        '''
        #assert side in ('home','away')
        if side == 'home':
            self.home_team_res.acc_team_score()
        else:
            self.away_team_res.acc_team_score()

    @assert_side_deco
    def acc_player_shoot(self,side,name,result):
        '''
        side: home, away
        name:
        result: Ture False
        '''
        #assert side in ('home','away')
        if side == 'home':
            self.home_team_res.acc_player_shoot_times(name,result)
        else:
            self.away_team_res.acc_player_shoot_times(name,result)


class TeamResult(object):
    '''
    Team Result
    '''
    def __init__(self, team_name, side, player_name_list):
        self.team_name = team_name
        self.side = side
        assert self.side in ("home","away")

        self.player1 = PlayerResult(player_name_list[0])
        self.player2 = PlayerResult(player_name_list[1])
        self.player3 = PlayerResult(player_name_list[2])
        self.player4 = PlayerResult(player_name_list[3])
        self.player5 = PlayerResult(player_name_list[4])

        self.score = 0

    def acc_team_score(self):
        self.score += 1

class PlayerResult(object):
    '''
    Player Result
    '''
    def __init__(self, name):
        self.name = name

        #attack
        self.shoot_success = 0
        self.shoot_fail = 0
        self.short_pass_success = 0
        self.short_pass_fail = 0
        self.long_pass_success = 0
        self.long_pass_fail = 0
        self.cross_success = 0
        self.cross_fail = 0
        self.dribbling_success = 0
        self.dribbling_fail = 0

        #defence 只有防守dribbling是个人行为，其他都是集体行为
        self.def_personal_dribbling_success = 0
        self.def_personal_dribbling_fail = 0
        self.def_team_shoot_success = 0
        self.def_team_shoot_fail = 0
        self.def_team_short_pass_success = 0
        self.def_team_short_pass_fail = 0
        self.def_team_long_pass_success = 0
        self.def_team_long_pass_fail = 0
        self.def_cross_success = 0
        self.def_cross_fail = 0

    def acc_shoot_success(self):
        self.shoot_success += 1

    def acc_shoot_fail(self):
        self.shoot_fail += 1

    def acc_short_pass_success(self):
        self.short_pass_success += 1

    def acc_short_pass_fail(self):
        self.short_pass_fail += 1

    def acc_long_pass_success(self):
        self.long_pass_success += 1

    def acc_long_pass_fail(self):
        self.long_pass_fail += 1

    def acc_cross_success(self):
        self.cross_success += 1

    def acc_cross_fail(self):
        self.cross_fail += 1

    def acc_dribbling_success(self):
        self.dribbling_success += 1

    def acc_dribbling_fail(self):
        self.dribbling_fail += 1

    def acc_def_personal_dribbling_success(self):
        self.def_personal_dribbling_success += 1

    def acc_def_personal_dribbling_fail(self):
        self.def_personal_dribbling_fail += 1

    def acc_def_team_shoot_success(self):
        self.def_team_shoot_success += 1

    def acc_def_team_shoot_fail(self):
        self.def_team_shoot_fail += 1

    def acc_def_team_short_pass_success(self):
        self.def_team_short_pass_success += 1

    def acc_def_team_short_pass_fail(self):
        self.def_team_short_pass_fail += 1

    def acc_def_team_long_pass_success(self):
        self.def_team_long_pass_success += 1

    def acc_def_team_long_pass_fail(self):
        self.def_team_long_pass_fail += 1

    def acc_def_cross_success(self):
        self.def_cross_success += 1

    def acc_def_cross_fail(self):
        self.def_cross_fail += 1



if __name__ == '__main__':
    a = Squad(side='home',team_name='a',mode='test')
    b = Squad(side='away',team_name='b',mode='test')
    g = GameResult(a,b)
    g.acc_score('home')
    print ""