#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.player import Player
from lib.utils import multy_random_one

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

    def get_player_list(self):
        return self.player_list

    def __str__(self):
        return self.team_name

    def get_player_by_att_ball_position(self, att_ball_position):
        players = []
        if att_ball_position == 'front':
            players = self.get_forward()
        elif att_ball_position == 'mid':
            players = self.get_mid()
        else:
            players = self.get_defence()
        return players

    def get_defence_player_by_att_ball_position(self, att_ball_position):
        players = []
        if att_ball_position == 'front':
            players = self.get_defence()
        elif att_ball_position == 'mid':
            players = self.get_mid()
        else:
            players = self.get_forward()
        return players

    def get_player_num(self, side, position):
        '''
        side: 进攻方 True  防守方 False
        position：进攻方球的位置
        '''
        if side:        #当前作为进攻方
            if position == 'front':
                return len(self.get_forward())
            elif position == 'mid':
                return len(self.get_mid())
            else:
                return len(self.get_defence())
        else:           #当前作为防守方
            if position == 'front':
                return len(self.get_defence())
            elif position == 'mid':
                return len(self.get_mid())
            else:
                return len(self.get_forward())

    def random_player(self, side, position):
        '''
        side: 进攻方 True  防守方 False
        position：进攻方球的位置
        '''
        if side:        #当前作为进攻方
            if position == 'front':
                return multy_random_one(self.get_forward())
            elif position == 'mid':
                return multy_random_one(self.get_mid())
            else:
                return multy_random_one(self.get_defence())
        else:           #当前作为防守方
            if position == 'front':
                return multy_random_one(self.get_defence())
            elif position == 'mid':
                return multy_random_one(self.get_mid())
            else:
                return multy_random_one(self.get_forward())

    def get_avg(self, players, attr):
        if not players:
            return 0
        values = [float(player.get_attr_value(attr)) for player in players]
        avg = sum(values) / len(values)
        return avg


    def get_avg_backfield_defence(self):
        players = self.get_defence()
        return self.get_avg(players, 'defence')


    def get_avg_backfield_marking(self):
        players = self.get_defence()
        return self.get_avg(players, 'marking')




    def get_short_pass_player_num(self, side, position):
        '''
        side: 进攻方 True  防守方 False
        position：进攻方球的位置
        '''
        if side:        #当前作为进攻方
            if position == 'back':
                return self.get_player_num(True,'back')+self.get_player_num(True,'mid')
            elif position == 'mid':
                return self.get_player_num(True,'mid')+self.get_player_num(True,'front')
        else:           #当前作为防守方
            if position == 'back':
                return self.get_player_num(False,'back')+self.get_player_num(False,'mid')
            elif position == 'mid':
                return self.get_player_num(False,'mid')+self.get_player_num(False,'front')

    def get_long_pass_player_num(self):
        '''
        无论进攻方防守方都取back和front
        '''
        return self.get_player_num(True,'back')+self.get_player_num(True,'front')



    # def get_short_pass_player(self, side ,position):
    #     '''
    #     side: 进攻方 True  防守方 False
    #     position：进攻方球的位置
    #     '''
    #     if side:        #当前作为进攻方
    #         if position == 'back':
    #             return self.get_player_num(True,'back')+self.get_player_num(True,'mid')
    #         elif position == 'mid':
    #             return self.get_player_num(True,'mid')+self.get_player_num(True,'front')
    #     else:           #当前作为防守方
    #         if position == 'back':
    #             return self.get_player_num(False,'back')+self.get_player_num(False,'mid')
    #         elif position == 'mid':
    #             return self.get_player_num(False,'mid')+self.get_player_num(False,'front')

    def get_single_field_avg(self, side, position, attr):
        '''
        position：进攻方球的位置
        attr: 属性
        '''
        if side:
            if position == 'back':
                players = self.get_player_by_att_ball_position('back')
            elif position == 'mid':
                players = self.get_player_by_att_ball_position('mid')
        else:
            if position == 'back':
                players = self.get_defence_player_by_att_ball_position('back')
            elif position == 'mid':
                players = self.get_defence_player_by_att_ball_position('mid')
        return self.get_avg(players,attr)

    def get_multy_field_avg(self, side ,position, attr):
        '''
        position：进攻方球的位置
        attr: 属性
        '''
        if side:
            if position == 'back':
                players = self.get_player_by_att_ball_position('back') + self.get_player_by_att_ball_position('mid')
            elif position == 'mid':
                players = self.get_player_by_att_ball_position('mid') + self.get_player_by_att_ball_position('front')
        else:
            if position == 'back':
                players = self.get_defence_player_by_att_ball_position('back') + self.get_defence_player_by_att_ball_position('mid')
            elif position == 'mid':
                players = self.get_defence_player_by_att_ball_position('mid') + self.get_defence_player_by_att_ball_position('front')
        return self.get_avg(players,attr)

    def get_cross_player_num(self, side, position):
        # if side:
        #     if position == 'back':
        #         return self.get_player_num(True,'back')
        #     elif position == 'mid':
        #         return self.get_player_num(True,'mid')
        # else:
        #     if position == 'back':
        #         return self.get_player_num(False,'back')
        #     elif position == 'mid':
        #         return self.get_player_num(False,'mid')
        return self.get_player_num(side,position)

    def player_move_in(self, player):
        #检查player是否在当前squad中
        assert player in self.get_player_list()
        if player in self.get_forward():  #球员在进攻方的最前场，报错
            raise Exception
        elif player in self.get_mid():
            self.forward.append(player)
            self.mid.remove(player)
        elif player in self.get_defence():
            self.mid.append(player)
            self.forward.remove(player)

if __name__ == '__main__':
    a = Squad(side='True',team_name='qq',mode='test')









