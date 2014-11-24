#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handler.squad import Squad
from data.player import Player
from conf.game_conf import BACKFIELD_ATT
from lib.utils import invert

class GameResult(object):
    '''
    Game Result
    '''
    def __init__(self, home_team, away_team):
        self.home_team_res = TeamResult(home_team.get_team_name(),home_team.get_side(),home_team.get_player_name_list())
        self.away_team_res = TeamResult(away_team.get_team_name(),away_team.get_side(),away_team.get_player_name_list())

    # def assert_side_player_name_deco(func):
    #     '''
    #     检查side是否正确，player name是否重复
    #     '''
    #     def _assert_side_player_name_deco(self,side,home_team_res,away_team_res)

    def print_result(self):
        print "Game Result:"
        for res in [self.home_team_res,self.away_team_res]:
            print res.team_name
            print "score:",res.score
            print "team possession time:",int(float(res.team_possession_time)/90.0)
            print "team shoot success:",res.team_shoot_success
            print "team shoot fail:",res.team_shoot_fail
            print "team short pass success:",res.team_short_pass_success
            print "team short pass fail:",res.team_short_pass_fail
            print "team long pass success:",res.team_long_pass_success
            print "team long pass fail:",res.team_long_pass_fail
            print "team cross success:",res.team_cross_success
            print "team cross fail:",res.team_cross_fail
            print "team dribbling success:",res.team_dribbling_success
            print "team dribbling fail:",res.team_dribbling_fail
            print ""
            print "team defence shoot success:",res.team_def_shoot_success
            print "team defence shoot fail:",res.team_def_shoot_fail
            print "team defence short pass success:",res.team_def_short_pass_success
            print "team defence short pass fail:",res.team_def_short_pass_fail
            print "team defence long pass success:",res.team_def_long_pass_success
            print "team defence long pass fail:",res.team_def_long_pass_fail
            print "team defence cross success:",res.team_def_cross_success
            print "team defence cross fail:",res.team_def_cross_fail
            print "team defence dribbling success:",res.team_def_dribbling_success
            print "team defence dribbling fail:",res.team_def_dribbling_fail

    def check_side_name_result_deco(func):
        '''
        Decorator 检查side name result
        '''
        def _check_side_name_result_deco(self,side,name,result):
            assert result in (True,False)
            assert side in ('home','away')
            return func(self,side,name,result)
        return _check_side_name_result_deco

    def check_side_name_list_result_deco(func):
        '''
        Decorator 检查 side name_list result
        '''
        def _check_side_name_list_result_deco(self,side,name_list,result):
            assert result in (True,False)
            assert side in ('home','away')
            return func(self,side,name_list,result)
        return _check_side_name_list_result_deco

    def check_side_deco(func):
        '''
        Decorator 检查side值是否正确
        '''
        def _assert_side_deco(self,side):
            assert side in ('home','away')
            return func(self,side)
        return _assert_side_deco

    @check_side_deco
    def acc_score(self, side):
        '''
        side: home, away
        '''
        #assert side in ('home','away')
        if side == 'home':
            self.home_team_res.acc_team_score()
        else:
            self.away_team_res.acc_team_score()

    @check_side_name_result_deco
    def acc_player_shoot(self, side, name, result):
        '''
        side: home, away
        name:
        result: Ture False
        '''
        if side == 'home':
            self.home_team_res.acc_player_shoot_times(name,result)
        else:
            self.away_team_res.acc_player_shoot_times(name,result)

    @check_side_name_result_deco
    def acc_player_short_pass(self, side, name, result):
        '''
        side: home, away
        name:
        result: True, False
        '''
        if side == 'home':
            self.home_team_res.acc_player_short_pass_times(name,result)
        else:
            self.away_team_res.acc_player_short_pass_times(name,result)

    @check_side_name_result_deco
    def acc_player_long_pass(self, side, name, result):
        '''
        side: home, away
        name:
        result: True, False
        '''
        if side == 'home':
            self.home_team_res.acc_player_long_pass_times(name,result)
        else:
            self.away_team_res.acc_player_long_pass_times(name,result)

    @check_side_name_list_result_deco
    def acc_team_att_cross(self, side, name_list, result):
        '''
        side: home, away
        name:
        result: True, False
        '''
        if side == 'home':
            self.home_team_res.acc_players_cross_times(name_list,result)
        else:
            self.away_team_res.acc_players_cross_times(name_list,result)

    @check_side_name_result_deco
    def acc_player_dribbling(self, side, name, result):
        '''
        side: home, away
        name:
        result: True, False
        '''
        if side == 'home':
            self.home_team_res.acc_player_dribbling_times(name,result)
        else:
            self.away_team_res.acc_player_dribbling_times(name,result)

    #defence
    @check_side_name_result_deco
    def acc_player_def_dribbling(self, side, name, result):
        '''
        side: home, away
        name:
        result: True, False
        '''
        if side == 'home':
            self.home_team_res.acc_player_def_dribbling_times(name,result)
        else:
            self.away_team_res.acc_player_def_dribbling_times(name,result)

    #@check_side_name_list_result_deco 不做检查，因为name_list可能为空，后防没有球员了
    def acc_team_def_shoot(self, side, name_list, result):
        '''
        side: home, away
        result: True, False
        name_list: def name list
        '''
        if len(name_list) != 0:        #后防队员数量不为0
            if side == 'home':
                self.home_team_res.acc_team_def_shoot_times(name_list,result)
            else:
                self.away_team_res.acc_team_def_shoot_times(name_list,result)

    @check_side_name_list_result_deco
    def acc_team_def_short_pass(self, side, name_list, result):
        '''
        side: home, away
        result: True, False
        name_list: def name list
        '''
        if side =='home':
            self.home_team_res.acc_team_def_short_pass_times(name_list,result)
        else:
            self.away_team_res.acc_team_def_short_pass_times(name_list,result)

    @check_side_name_list_result_deco
    def acc_team_def_long_pass(self, side, name_list, result):
        '''
        side: home, away
        result: True, False
        name_list: def name list
        '''
        if side =='home':
            self.home_team_res.acc_team_def_long_pass_times(name_list,result)
        else:
            self.away_team_res.acc_team_def_long_pass_times(name_list,result)

    @check_side_name_list_result_deco
    def acc_team_def_cross(self, side, name_list, result):
        '''
        side: home, away
        result: True, False
        name_list: def name list
        '''
        if side =='home':
            self.home_team_res.acc_team_def_cross_times(name_list,result)
        else:
            self.away_team_res.acc_team_def_cross_times(name_list,result)

    def get_side_by_player_name(self, name):
        '''
        通过name判断是哪一方的球员
        '''
        if self.home_team_res.name_exist(name):
            return 'home'
        elif self.away_team_res.name_exist(name):
            return 'away'
        else:
            print "ERROR, shoot player error",name
            raise Exception

    #set_shoot_result(result=res,player=shoot_player,defence_players=defence_players)
    def set_shoot_result(self, result, player, defence_players):
        '''
        通过shoot_player 所在的队来判断哪个队增加一分，队员名称不能有重复
        '''
        name = player.get_name()
        defence_names_list = self.get_names(defence_players)
        side = self.get_side_by_player_name(name)
        if result:
            self.acc_score(side)
        self.acc_player_shoot(side,name,result)
        self.acc_team_def_shoot(invert(side),defence_names_list,invert(result))

    def set_short_pass_result(self, result, player, defence_players):
        name = player.get_name()
        defence_names_list = self.get_names(defence_players)
        side = self.get_side_by_player_name(name)
        self.acc_player_short_pass(side,name,result)
        self.acc_team_def_short_pass(invert(side),defence_names_list,invert(result))

    def set_long_pass_result(self, result, player, defence_players):
        name = player.get_name()
        defence_names_list = self.get_names(defence_players)
        side = self.get_side_by_player_name(name)
        self.acc_player_long_pass(side,name,result)
        self.acc_team_def_long_pass(invert(side),defence_names_list,invert(result))

    def set_cross_result(self, result, attack_players, defence_players):
        name = attack_players[0].get_name()
        attack_names_list = self.get_names(attack_players)
        defence_names_list = self.get_names(defence_players)
        side = self.get_side_by_player_name(name)
        #self.acc_players_cross(side,attack_names_list,result)
        self.acc_team_att_cross(side,attack_names_list,result)
        self.acc_team_def_cross(invert(side),defence_names_list,invert(result))

    def set_dribbling_result(self, result, attack_player, def_player):
        attack_player_name = attack_player.get_name()
        side = self.get_side_by_player_name(attack_player_name)
        self.acc_player_dribbling(side,attack_player_name,result)
        self.acc_player_def_dribbling(invert(side),def_player.get_name(),invert(result))

    def get_names(self,players):
        return [i.get_name() for i in players]

    def cal_both_team_result(self):
        self.home_team_res.cal_team_result()
        self.away_team_res.cal_team_result()

    def add_team_possesion(self, ball_side):
        assert ball_side in (True,False)
        if ball_side:
            self.home_team_res.acc_possesion()
        else:
            self.away_team_res.acc_possesion()









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
        self.team_possession_time = 0

    # def get_all_player_result(self,attack_way,result):
    #     count = 0
    #     for player in [self.player1,self.player2,self.player3,self.player4,self.player5]:
    #         count +=

    def get_team_attack_result(self, attack_way, result):
        assert attack_way in BACKFIELD_ATT
        assert result in (True,False)
        count = 0
        for player in [self.player1,self.player2,self.player3,self.player4,self.player5]:
            if attack_way == 'shoot':
                if result:
                    count += player.shoot_success
                else:
                    count += player.shoot_fail
            elif attack_way == 'short_pass':
                if result:
                    count += player.short_pass_success
                else:
                    count += player.short_pass_fail
            elif attack_way == 'long_pass':
                if result:
                    count += player.long_pass_success
                else:
                    count += player.long_pass_fail
            elif attack_way == 'cross':
                if result:
                    count += player.cross_success
                else:
                    count += player.cross_fail
            elif attack_way == 'dribbling':
                if result:
                    count += player.dribbling_success
                else:
                    count += player.dribbling_fail
        return count

    def get_team_def_result(self, defence_way, result):
        #assert defence_way in BACKFIELD_ATT
        assert result in (True,False)
        count = 0
        for player in [self.player1,self.player2,self.player3,self.player4,self.player5]:
            if defence_way == 'def_shoot':
                if result:
                    count += player.def_team_shoot_success
                else:
                    count += player.def_team_shoot_fail
            elif defence_way == 'def_short_pass':
                if result:
                    count += player.def_team_short_pass_success
                else:
                    count += player.def_team_short_pass_fail
            elif defence_way == 'def_long_pass':
                if result:
                    count += player.def_team_long_pass_success
                else:
                    count += player.def_team_long_pass_fail
            elif defence_way == 'def_cross':
                if result:
                    count += player.def_team_cross_success
                else:
                    count += player.def_team_cross_fail
            elif defence_way == 'def_dribbling':
                if result:
                    count += player.def_personal_dribbling_success
                else:
                    count += player.def_personal_dribbling_fail
        return count

    def cal_team_result(self):
        '''
        比赛完成后计算team数值
        '''
        self.team_shoot_success = self.get_team_attack_result('shoot',True)
        self.team_shoot_fail = self.get_team_attack_result('shoot',False)
        self.team_short_pass_success = self.get_team_attack_result('short_pass',True)
        self.team_short_pass_fail = self.get_team_attack_result('short_pass',False)
        self.team_long_pass_success = self.get_team_attack_result('long_pass',True)
        self.team_long_pass_fail = self.get_team_attack_result('long_pass',False)
        self.team_cross_success = self.get_team_attack_result('cross',True)
        self.team_cross_fail = self.get_team_attack_result('cross',False)
        self.team_dribbling_success = self.get_team_attack_result('dribbling',True)
        self.team_dribbling_fail = self.get_team_attack_result('dribbling',False)

        self.team_def_shoot_success = self.get_team_def_result('def_shoot',True)
        self.team_def_shoot_fail = self.get_team_def_result('def_shoot',False)
        self.team_def_short_pass_success = self.get_team_def_result('def_short_pass',True)
        self.team_def_short_pass_fail = self.get_team_def_result('def_short_pass',False)
        self.team_def_long_pass_success = self.get_team_def_result('def_long_pass',True)
        self.team_def_long_pass_fail = self.get_team_def_result('def_long_pass',False)
        self.team_def_cross_success = self.get_team_def_result('def_cross',True)
        self.team_def_cross_fail = self.get_team_def_result('def_cross',False)
        self.team_def_dribbling_success = self.get_team_def_result('def_dribbling',True)
        self.team_def_dribbling_fail = self.get_team_def_result('def_dribbling',False)

        self.score = self.team_shoot_success

    def check_name_result_deco(func):
        '''
        Decorator 检查side值是否正确,name是否存在self队中
        '''
        def _assert_name_result_deco(self,name,result):
            assert result in (True,False)
            if not self.name_exist(name):
                print name," not in this team"
                raise Exception
            return func(self,name,result)
        return _assert_name_result_deco

    def check_name_list_result_deco(func):
        '''
        Decorator 检查name_list result
        '''
        def _check_name_list_deco(self,name_list,result):
            assert result in (True,False)
            for name in name_list:
                if not self.name_exist(name):
                    print name,"not in this team"
                    raise Exception
            return func(self,name_list,result)
        return _check_name_list_deco

    def get_name_list(self):
        return [player.get_name() for player in [self.player1,self.player2,self.player3,self.player4,self.player5]]

    def name_exist(self, name):
        name_list = self.get_name_list()
        return name in name_list

    def acc_team_score(self):
        self.score += 1

    def get_player_by_name(self, name):
        for player in [self.player1,self.player2,self.player3,self.player4,self.player5]:
            if player.get_name() == name:
                return player
        return False

    def get_player_list_by_name_list(self, name_list):
        res = []
        for name in name_list:
            player = self.get_player_by_name(name)
            res.append(player)
        return res

    @check_name_result_deco
    def acc_player_shoot_times(self, name, result):
        '''
        name: player name
        resutl: True False
        '''
        p = self.get_player_by_name(name)
        if not p:
            print "ERROR,can not get player:",name
            raise Exception
        if result:
            p.acc_shoot_success()
        else:
            p.acc_shoot_fail()

    @check_name_result_deco
    def acc_player_short_pass_times(self , name, result):
        '''
        name: player name
        resutl: True False
        '''
        p = self.get_player_by_name(name)
        if not p:
            print "ERROR,can not get player:",name
            raise Exception
        if result:
            p.acc_short_pass_success()
        else:
            p.acc_short_pass_fail()

    @check_name_result_deco
    def acc_player_long_pass_times(self, name, result):
        p = self.get_player_by_name(name)
        if not p:
            print "ERROR,can not get player:",name
            raise Exception
        if result:
            p.acc_long_pass_success()
        else:
            p.acc_long_pass_fail()

    @check_name_list_result_deco
    def acc_players_cross_times(self, name_list, result):
        p_list = self.get_player_list_by_name_list(name_list)
        if not p_list:
            print "ERROR,can not get player:",name_list
            raise Exception
        for p in p_list:
            if result:
                p.acc_cross_success()
            else:
                p.acc_cross_fail()

    @check_name_result_deco
    def acc_player_dribbling_times(self, name, result):
        p = self.get_player_by_name(name)
        if not p:
            print "ERROR,can not get player:",name
            raise Exception
        if result:
            p.acc_dribbling_success()
        else:
            p.acc_dribbling_fail()

    @check_name_result_deco
    def acc_player_def_dribbling_times(self, name, result):
        p = self.get_player_by_name(name)
        if not p:
            print "ERROR,can not get player:",name
            raise Exception
        if result:
            p.acc_def_personal_dribbling_success()
        else:
            p.acc_def_personal_dribbling_fail()

    #@check_name_list_result_deco
    def acc_team_def_shoot_times(self, name_list, result):
        p_list = self.get_player_list_by_name_list(name_list)
        if not p_list:
            print "ERROR, can not get player list",name_list
            raise Exception
        for p in p_list:
            if result:
                p.acc_def_team_shoot_success()
            else:
                p.acc_def_team_shoot_fail()

    @check_name_list_result_deco
    def acc_team_def_short_pass_times(self, name_list, result):
        p_list = self.get_player_list_by_name_list(name_list)
        if not p_list:
            print "ERROR, can not get player list",name_list
            raise Exception
        for p in p_list:
            if result:
                p.acc_def_team_short_pass_success()
            else:
                p.acc_def_team_short_pass_fail()

    @check_name_list_result_deco
    def acc_team_def_long_pass_times(self, name_list, result):
        p_list = self.get_player_list_by_name_list(name_list)
        if not p_list:
            print "ERROR, can not get player list",name_list
            raise Exception
        for p in p_list:
            if result:
                p.acc_def_team_long_pass_success()
            else:
                p.acc_def_team_long_pass_fail()

    @check_name_list_result_deco
    def acc_team_def_cross_times(self, name_list, result):
        p_list = self.get_player_list_by_name_list(name_list)
        if not p_list:
            print "ERROR, can not get player list",name_list
            raise Exception
        for p in p_list:
            if result:
                p.acc_def_team_cross_success()
            else:
                p.acc_def_team_cross_fail()

    def acc_possesion(self):
        self.team_possession_time += 1














class PlayerResult(object):
    '''
    Player Result
    '''
    def __init__(self, name):
        self.name = name

        #attack 所有的进攻都是个人行为
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
        self.def_team_cross_success = 0
        self.def_team_cross_fail = 0

    def get_name(self):
        return self.name

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

    def acc_def_team_cross_success(self):
        self.def_team_cross_success += 1

    def acc_def_team_cross_fail(self):
        self.def_team_cross_fail += 1

if __name__ == '__main__':
    a = Squad(side='home',team_name='a',mode='test')
    b = Squad(side='away',team_name='b',mode='test')
    g = GameResult(a,b)
    # g.acc_score('home')
    # g.acc_player_shoot(side='home',name='test2',result=False)
    # g.acc_player_short_pass(side='home',name='test1',result=True)
    # g.acc_player_long_pass(side='home',name='test1',result=True)
    # #g.acc_player_cross(side='home',name='test1',result=True)
    # g.acc_player_dribbling(side='home',name='test1',result=True)
    #

    # g.acc_team_def_cross(side='home',name_list=['test1','test2'],result=True)
    # g.acc_team_def_long_pass(side='home',name_list=['test1','test2'],result=True)
    # g.acc_team_def_short_pass(side='home',name_list=['test1','test2'],result=True)
    # g.acc_player_def_dribbling(side='home',name='test1',result=True)

    players = a.get_mid()
    g.set_dribbling_result(False,a.get_forward()[0],b.get_defence()[0])
    g.cal_both_team_result()
    print ""
