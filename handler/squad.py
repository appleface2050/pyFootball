#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.player import Player
from lib.utils import multy_random_one
from conf.game_conf import MIN_ATTR_VALUE


import copy

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

        self.inital_forward = []
        self.inital_mid = []
        self.inital_defence = []
        self.inital_player_list = []

        self.prepare_game()

        if mode == 'test':
            self.player_list = self.init_test_players()
            self.init_test_squad()
            self.strategy = self.init_test_strategy()

        self.prepare_game()

    def prepare_game(self):
        self.inital_forward = copy.deepcopy(self.forward)
        self.inital_mid = copy.deepcopy(self.mid)
        self.inital_defence = copy.deepcopy(self.defence)
        self.inital_player_list = copy.deepcopy(self.player_list)

    def reset_squad(self):
        # self.forward = self.inital_squad['forward']
        # self.mid = self.inital_squad['mid']
        # self.defence = self.inital_squad['defence']
        self.forward = copy.deepcopy(self.inital_forward)
        self.mid = copy.deepcopy(self.inital_mid)
        self.defence = copy.deepcopy(self.inital_defence)
        self.player_list = copy.deepcopy(self.inital_player_list)

    def init_test_players(self):
        players = []
        for i in xrange(1,6):
            players.append(Player(name=('test'+str(i))))
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

    def get_player_name_list(self):
        return [player.get_name() for player in self.player_list]

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

    def get_forward_name(self):
        return [p.name for p in self.get_forward()]

    def get_mid_name(self):
        return [p.name for p in self.get_mid()]

    def get_defence_name(self):
        return [p.name for p in self.get_defence()]

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
            return MIN_ATTR_VALUE
        values = [float(player.get_attr_value(attr)) for player in players]
        avg = sum(values) / len(values)
        #if avg == 0:
        #    avg = MIN_ATTR_VALUE
        return avg

    def get_avg_backfield_defence(self):
        players = self.get_defence()
        return self.get_avg(players, 'defence')

    def get_avg_backfield_marking(self):
        players = self.get_defence()
        return self.get_avg(players, 'marking')

    def reset_squad(self):
        self.forward = copy.deepcopy(self.inital_forward)
        self.mid = copy.deepcopy(self.inital_mid)
        self.defence = copy.deepcopy(self.inital_defence)

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

    def get_defence_player_number(self):
        return len(self.defence)

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
        assert player.name in [p.get_name() for p in self.get_player_list()]
        if player.get_name() in self.get_forward_name():  #球员在进攻方的最前场，报错
            raise Exception
        elif player.get_name() in self.get_mid_name():
            self.forward.append(player)
            self.mid = self.remove_by_player_name(self.mid,player.get_name())
        elif player.get_name() in self.get_defence_name():
            self.mid.append(player)
            self.defence = self.remove_by_player_name(self.defence,player.get_name())

    def player_disappear(self, player_name):
        #检查player是否在当前squad的backfield中
        assert player_name in [player.get_name() for player in self.get_defence()]
        self.player_list = self.remove_by_player_name(self.player_list,player_name)
        self.defence = self.remove_by_player_name(self.defence,player_name)


    def print_inital_squad(self):
        print self.inital_defence
        print self.inital_mid
        print self.inital_forward

    def print_current_squad(self):
        print self.get_defence()
        print self.get_mid()
        print self.get_forward()

    def remove_by_player_name(self, player_list, player_name):
        assert player_name in [p.get_name() for p in player_list]
        res = []
        for i in player_list:
            if i.get_name() == player_name:
                continue
            else:
                res.append(i)
        return res

    def print_desc(self):
        print "defence:",self.get_defence(),"mid:",self.get_mid(),"forword:",self.get_forward()



if __name__ == '__main__':
    a = Squad(side='True',team_name='qq',mode='test')
    print 'start'
    a.print_current_squad()
    print 'change'
    move_in_player = a.get_defence()[0]
    #a.player_move_in(move_in_player)
    #a.print_current_squad()

    a.player_disappear(move_in_player.get_name())

    #a.mid = a.remove_by_player_name(a.mid,move_in_player.get_name())
    #print a.get_player_list()
    a.print_desc()
    print a.get_player_num(True,'mid')

    # print a.get_defence()
    # print a.get_mid()
    # print a.get_forward()
    # a.print_inital_squad()
    # a.reset_squad()
    # print 'reset'
    # print a.get_defence()
    # print a.get_mid()
    # print a.get_forward()





