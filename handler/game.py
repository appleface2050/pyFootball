#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from handler.team import Squad
from conf.game_conf import BACKFIELD_ATT,MIDFIELD_ATT,FRONTFIELD_ATT

class Match(object):
    '''
    Match
    '''
    def __init__(self,mode=None):
        self.mode = mode
        self.home_team = ''
        self.away_team = ''

        self.ball_side = True  #True 主队球权   False 客队球权
        self.ball_positoin = None # 1 2 3 分别代表主队眼中的后场 中场 前场

        if mode == 'test':
            self.init_test_game()


    def init_test_game(self):
        self.home_team = Squad(side='home',team_name='测试队1',mode='test')
        self.away_team = Squad(side='away',team_name='测试队2',mode='test')

    def run(self):
        for m_time in xrange(0,90):
            self.ball_positoin = 1
            self.match(self.home_team,self.away_team,self.ball_side)


    def match(self, home_team, away_team, ball_side):
        '''
        根据球权判断进攻方
        '''

        if self.ball_side: #主队球权
            self.attack(self.home_team,self.away_team,self.ball_positoin)  #主队进攻
        else:
            self.attack(self.away_team,self.home_team,self.ball_positoin)  #客队进攻

    def attack(self, att_team, defence_team, position):
        '''
        根据球的位置判断进攻方式和进攻防守人员
        '''
        if position == 1:             #后场
            att_way = self.generate_attack_way(att_team.get_strategy(),BACKFIELD_ATT,att_team.get_defence())                     #这里设置进攻策略
            self.compare(att_team,defence_team,att_way,position)


        elif position == 2:            #中场
            pass
        elif position == 3:            #前场
            pass

        #self.finish_attack()

    def compare(self, att_team, defence_team, att_way, position):
        print att_team,defence_team,att_way,position

    def generate_attack_way(self, att_team_strategy, att_field_position, att_players):
        if not att_team_strategy:
            if len(att_players) < 2:    #人数少于2个去掉cross进攻方式
                att_field_position = self.delete_cross(att_field_position)
            return self.random_attack_way(att_field_position)
        else:
            #not ready yet
            return self.random_attack_way(att_field_position)

    def random_attack_way(self, att_field_position):
        count = len(att_field_position)
        return att_field_position[random.randint(0,count-1)]

    def delete_cross(self, att_field_position):
        if 'cross' in att_field_position:
            att_field_position.remove('cross')
        return att_field_position

if __name__ == '__main__':
    a = Match(mode='test')
    a.run()




