#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handler.squad import Squad
from conf.game_conf import BACKFIELD_ATT,MIDFIELD_ATT,FRONTFIELD_ATT,ATT_BALL_POSITION
from data.exceptions import MatcheException
from lib.utils import multy_random_one,random_result

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
        #self.att_ball_positon = None #进攻方球的位置 ['front','mid','back']

        self.home_score = 0
        self.away_score = 0

        if mode == 'test':
            self.init_test_game()

    def att_ball_position(self):
        if self.ball_positoin == 1:
            if self.ball_side == True:
                return 'back'
            else:
                return 'front'
        elif self.ball_positoin == 2:
            return 'mid'
        elif self.ball_positoin == 3:
            if self.ball_side == True:
                return 'front'
            else:
                return 'back'
        else:
            print "ERROR... att_ball_position"
            raise MatcheException

    def init_test_game(self):
        self.home_team = Squad(side='home',team_name='测试队1',mode='test')
        self.away_team = Squad(side='away',team_name='测试队2',mode='test')


    def run(self):
        self.ball_positoin = 2           #主队中场开始进攻
        for m_time in xrange(1,91):
            if not self.data_check():
                raise Exception
            print 'time: ',m_time
            self.match_begin(self.home_team,self.away_team,self.ball_side)

    def data_check(self):
        '''
        验证数据是否正确
        '''





    def match_begin(self, home_team, away_team, ball_side):
        '''
        根据球权判断进攻方
        '''
        if self.ball_side: #主队球权
            print "主队进攻..."
            self.attack(self.home_team,self.away_team,self.att_ball_position())  #主队进攻
        else:
            print "客队进攻..."
            self.attack(self.away_team,self.home_team,self.att_ball_position())  #客队进攻


    def attack(self, att_team, defence_team, att_ball_position):
        '''
        根据球的位置判断进攻方式和进攻防守人员
        '''
        assert att_ball_position in ATT_BALL_POSITION       #进攻方位置
        att_way = self.generate_attack_way(att_team.get_strategy(),att_ball_position,att_team,defence_team)     #这里设置进攻策略
        result = self.compare(att_team,defence_team,att_way,att_ball_position)
        print "result:",result
        self.finish_attack(att_way,result,att_team, defence_team)            #根据结果设置状态

    def finish_attack(self, att_way, result, att_team, defence_team):
        if att_way == 'shoot':
            if result:  #进球进攻方分数加一，转换球权，球位置设为中场
                self.acc_one_score()
                self.after_goal_reset()

            else:       #未进球转换球权，球位置设为转换球权后的持球方后场
                self.change_ball_side()
                #self.set_ball_position('back')
                self.set_ball_position_attack_back()
            self.reset_both_side_squad()

        elif att_way == 'short_pass':
            if result:  #传球成功位置进一格
                self.set_acc_ball_position()
            else:       #传球失败交换球权
                self.change_ball_side()

        elif att_way == 'long_pass':
            if result:  #长传成功设置球位置为进攻方前场
                self.set_ball_position_attack_front()
            else:       #长传失败转换持球权，设置球位置为进攻方后场
                self.change_ball_side()
                self.set_ball_position_attack_back()
                self.reset_both_side_squad()

        elif att_way == 'cross':
            if result:  #cross成功位置进一格
                self.set_acc_ball_position()
            else:
                self.change_ball_side()

        elif att_way == 'dribbling':
            res,dribbling_player,defence_player = result[0], result[1], result[2]
            if res:  #过人成功球位置进一格，如果不在前场，当前阵容过人的人前进一格  如果当前是在前场，则减少一名防守球员
                if (self.ball_side and self.ball_positoin != 3) or (self.ball_side == 0 and self.ball_positoin != 1): #主队进攻且球位置不在攻方前场,或客队进攻且球位置不在进攻方前场
                    self.set_player_move_in(dribbling_player)
                    self.set_acc_ball_position() #最后球位置进一格
                else:           #如果是在前场防守方减少一名队员
                    self.set_player_disappear(defence_player)
            else:       #过人失败交换球权
                self.change_ball_side()

    def reset_both_side_squad(self):
        '''
        用于取消过人成功后的squad变动
        reset条件：长传失败，射门失败
        '''
        self.home_team.reset_squad()
        self.away_team.reset_squad()

    def set_player_move_in(self, player):
        #检查player是否是在当前的进攻方，如果不是报错
        assert player.get_name() in self.current_attack_team_players_name()
        if self.ball_side:
            self.home_team.player_move_in(player)
        else:
            self.away_team.player_move_in(player)

    def set_player_disappear(self, player):
        #检查player是否在当前防守方的后场，如果不是报错
        assert player.get_name() in self.current_defence_team_backfield_players_name()
        if self.ball_side:
            self.away_team.player_disappear(player.get_name())
        else:
            self.home_team.player_disappear(player.get_name())

    def current_attack_team_players_name(self):
        if self.ball_side:
            return self.home_team.get_player_name_list()
        else:
            return self.away_team.get_player_name_list()

    def current_defence_team_backfield_players_name(self):
        if self.ball_side:
            return [player.get_name() for player in self.away_team.get_defence()]
        else:
            return [player.get_name() for player in self.home_team.get_defence()]

    def set_ball_position_attack_back(self):
        '''
        设置球位置为进攻方后场
        '''
        if self.ball_side:
            self.ball_positoin = 1
        else:
            self.ball_positoin = 3

    def set_ball_position_attack_front(self):
        '''
        设置球位置为进攻方前场
        '''
        if self.ball_side:
            self.ball_positoin = 3
        else:
            self.ball_positoin = 1

    def set_acc_ball_position(self):
        '''
        球的位置在当前位置的基础上前进一步
        '''
        if self.ball_side:
            self.ball_positoin += 1
        else:
            self.ball_positoin -= 1
        assert self.ball_positoin in (1,2,3)


    # def set_ball_position(self,position):
    #     '''
    #     根据当前球权方和想要设置的位置设置球的位置
    #     '''
    #
    #     if self.ball_side:   #主队球权
    #         if position == 'back':
    #             self.ball_positoin = 1
    #         elif position == 'mid':
    #             self.ball_positoin = 2
    #         elif position == 'front':
    #             self.ball_positoin = 3
    #     else:               #客队球权
    #         if position == 'back':
    #             self.ball_positoin = 3
    #         elif position == 'mid':
    #             self.ball_positoin = 2
    #         elif position == 'front':
    #             self.ball_positoin = 1


    def after_goal_reset(self):
        self.change_ball_side()
        self.ball_positoin = 2

    def acc_one_score(self):
        if self.ball_side:
            self.home_score += 1
        else:
            self.away_score += 1

    def change_ball_side(self):
        '''
        转换球权
        '''
        if self.ball_side:
            self.ball_side = False
        else:
            self.ball_side = True

    def generate_attack_way(self, att_team_strategy, att_ball_position, att_team, defence_team):
        '''
        BACKFIELD_ATT = ['shoot','short_pass','long_pass','cross','dribbling']
        MIDFIELD_ATT = ['shoot','short_pass','cross','dribbling']
        FRONTFIELD_ATT = ['shoot','cross','dribbling']

        '''
        assert att_ball_position in ATT_BALL_POSITION
        att_ways = []
        if not att_team_strategy:       #未设置特殊的战术
            if att_ball_position == 'back':
                att_ways = BACKFIELD_ATT
            elif att_ball_position == 'mid':
                att_ways = MIDFIELD_ATT
            else:
                if defence_team.get_defence_player_number() == 0:      #过完最后一个人的情况，防守方后卫人数为0
                    att_ways = ['shoot']
                else:
                    att_ways = FRONTFIELD_ATT
        else:
            #not ready yet
            pass

        #去除2个人不到的情况下不能使用cross的情况
        att_ways = self.delete_cross(att_ways,att_team,att_ball_position)
        #去除过了最后一个人的情况

        return multy_random_one(att_ways)

    def compare(self, att_team, defence_team, att_way, position):
        print " 进攻方:",
        att_team.print_desc()
        print " 防守方:",
        defence_team.print_desc()
        print '进攻方式:',att_way,' ball position:',position
        print "comparing..."
        if att_way == 'shoot':
            res = self.cal_shoot_res(att_team,defence_team,position)
        elif att_way == 'short_pass':
            res = self.cal_short_pass_res(att_team,defence_team,position)
        elif att_way == 'long_pass':
            res = self.cal_long_pass_res(att_team,defence_team,position)
        elif att_way == 'cross':
            res = self.cal_cross_res(att_team,defence_team,position)
        elif att_way == 'dribbling':
            res = self.cal_dribbling_res(att_team,defence_team,position)
        return res
    # def random_attack_way(self, att_field_position):
    #     count = len(att_field_position)
    #     return att_field_position[random.randint(0,count-1)]

    def delete_cross(self, att_ways, att_team, att_ball_position):
        if 'cross' not in att_ways:
            return att_ways
        else:
            players = att_team.get_player_by_att_ball_position(att_ball_position)
            if len(players) < 2:
                att_ways.remove('cross')
            return att_ways

    def cal_shoot_res(self, att_team, defence_team, position):
        '''
        射门结果计算公式：
        基础分数/(防守线人数+1) * （射门人进攻值*射门人射门值） / （防守方后场人员防守平均值*防守方后场人员平均mark值）
        前场base = 700
        中场base = 140
        后场base = 25
        '''
        assert position in ATT_BALL_POSITION
        shoot_player = att_team.random_player(side='True',position=position)
        if not shoot_player:
            print "ERROR, shoot_player is None"
            raise MatcheException

        if position == 'back':
            base = 25.0
        elif position == 'mid':
            base = 140.0
        else:
            base = 700.0
        score = base / \
                float(defence_team.get_player_num(side=False,position=position)+1) * \
                float(shoot_player.get_offensive() * shoot_player.get_finish()) / float((defence_team.get_avg_backfield_defence() * \
                                                                              defence_team.get_avg_backfield_marking()))
        return random_result(score)

    def cal_short_pass_res(self, att_team, defence_team, position):
        '''
        计算短传结果公式：
        参与方：当前field和下一个field
        基础传球分数 * (进攻方人数/防守方人数) * （多个field进攻方平均进攻值*传球队员传球值/（多field防守方平均防守值*防守方人员平均mark值）
        base = 800
        '''
        assert position in ('back','mid')
        pass_player = att_team.random_player(side=True,position=position)
        base = 800.0
        score = base * \
                (float(att_team.get_short_pass_player_num(True,position)) / float(att_team.get_short_pass_player_num(False,position))) * \
                float(att_team.get_multy_field_avg(side=True,position=position,attr='offensive') * pass_player.get_short_pass()) / \
                float(defence_team.get_multy_field_avg(side=False,position=position,attr='defence') * \
                 defence_team.get_multy_field_avg(side=False,position=position,attr='marking'))
        return random_result(score)

    def cal_long_pass_res(self, att_team, defence_team, position):
        '''
        计算长传结果公式：
        参与方：后场和前场
        基础长传分数 * （进攻方人数/防守方人数） * (多个field进攻方平均进攻值*传球队员长传值/（多field防守方平均防守值*防守方后场平均mark值）)
        base = 500
        '''
        assert position in ('back')
        pass_player = att_team.random_player(side=True,position=position)
        base = 500.0
        score = base * \
                float(att_team.get_long_pass_player_num() / defence_team.get_long_pass_player_num()) * \
                float(att_team.get_multy_field_avg(side=True,position=position,attr='offensive') * pass_player.get_long_pass()) / \
                float(defence_team.get_multy_field_avg(side=False,position=position,attr='defence') * \
                 defence_team.get_multy_field_avg(side=False,position=position,attr='marking'))
        return random_result(score)

    def cal_cross_res(self, att_team, defence_team, position):
        '''
        计算推进的结果:
        参与方: 当前field
        基础cross分数 * (进攻方人数/防守方人数) * （进攻方平均进攻值*进攻方平均传球值）/ （（防守方人员防守平均值*防守方后场平均mark值））
        base = 800
        '''
        assert position in ('back','mid')
        base = 800.0
        score = base * \
                (float(att_team.get_cross_player_num(side=True,position=position)) / float(defence_team.get_cross_player_num(side=False,position=position))) * \
                float(att_team.get_single_field_avg(side=True,position=position,attr='offensive')) * \
                float(att_team.get_single_field_avg(side=True,position=position,attr='short_pass')) / \
                float((defence_team.get_single_field_avg(side=False,position=position,attr='defence')) *\
                (defence_team.get_single_field_avg(side=False,position=position,attr='marking')))
        return random_result(score)

    def cal_dribbling_res(self, att_team, defence_team, position):
        '''
        计算过人的结果:
        参与方：当前field
        基础dribbling分数 * （进攻执行人进攻值*执行人dribbling）/ （防守执行人防守值*防守执行人marking）
        base = 500
        '''
        dribbling_player = att_team.random_player(side=True,position=position)
        defence_player = defence_team.random_player(side=False,position=position)
        base = 500.0
        score = base * \
                float(dribbling_player.get_offensive() * dribbling_player.get_dribbling()) / \
                float(defence_player.get_defence() * defence_player.get_marking())
        res = random_result(score)
        return [res,dribbling_player,defence_player]

if __name__ == '__main__':
    a = Match(mode='test')
    a.run()




