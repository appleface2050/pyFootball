#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import datetime

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

class Player(object):
    '''
    player in club
    '''
    def __init__(self,mode=None):
        self.name = ''
        self.birthdate = ''
        self.age = ''
        self.salary = 0;

        self.offensive = 0;
        self.defence = 0;

        self.dribbling = 0;
        self.short_pass = 0;
        self.long_pass = 0;
        self.finish = 0;
        self.marking = 0;

        if mode == 'test':
            self.init_test_player()


        #save
        #self.stamina = 0;

    def init_test_player(self):

        self.name = 'test'
        self.birthdate = datetime.datetime.strptime('1990-01-01','%Y-%m-%d').date()
        self.age = self.cal_player_age(self.birthdate)

        self.offensive = 10
        self.defence = 10

        self.dribbling = 10
        self.short_pass = 10
        self.long_pass = 10
        self.finish = 10
        self.marking = 10


    def cal_player_age(self, birthdate):
        now = datetime.datetime.now().date()
        a = now - birthdate
        return a.days/365

    def __str__(self):
        return 'name:'+(self.name)+'    offensive:'+str(self.offensive)+'   defence:'\
               +str(self.defence)+'    dribbling:'+str(self.dribbling)\
               +'   short pass:'+str(self.short_pass)+' long pass:'+str(self.long_pass)\
               +'   finish:'+str(self.finish)\
               +'   marking:'+str(self.marking)

    def get_name(self):
        return self.name

    def get_birthdate(self):
        return self.birthdate

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary

    def get_offensive(self):
        return self.offensive

    def get_defence(self):
        return self.defence

    def get_dribbling(self):
        return self.dribbling

    def get_short_pass(self):
        return self.short_pass

    def get_long_pass(self):
        return self.long_pass

    def get_finish(self):
        return self.finish

    def get_marking(self):
        return self.marking

    def get_attr_value(self, attr):
        assert attr in ('offensive','defence','dribbling','short_pass','long_pass','finish','marking')
        if attr == 'offensive':
            return self.get_offensive()
        elif attr == 'defence':
            return self.get_defence()
        elif attr == 'dribbling':
            return self.get_dribbling()
        elif attr == 'short_pass':
            return self.get_short_pass()
        elif attr == 'long_pass':
            return self.get_long_pass()
        elif attr == 'finish':
            return self.get_finish()
        elif attr == 'marking':
            return self.get_marking()
        else:
            raise Exception


if __name__ == '__main__':
    a = Player(mode='test')
    print a

