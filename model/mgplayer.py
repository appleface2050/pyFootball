#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import datetime

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

from lib.mongodb import MGModel

class MGPlayer(MGModel):
    '''
    player
    '''
    _db = 'fb'
    _collection = 'player'

    def generate_test_players(self,name_start,name_end,value):
        '''
        自动生成球员
        name_start: 11
        name_end: 20
        value: 11
        '''

        now = datetime.datetime.now()
        while(name_start<=name_end):
            data = {
          "name" : "",
          "age" : 0,
          "salary" : 0,
          "offensive" : 10,
          "defence" : 10,
          "dribbling" : 10,
          "short_pass" : 10,
          "long_pass" : 10,
          "finish" : 10,
          "marking" : 10,
          "uptime" : "2014-11-25"
        }
            data['name'] = "test"+str(name_start)
            data['uptime'] = now.strftime(('%Y-%m-%d'))
            if value:
                for key in data.keys():
                    if key not in ('name','birthdate','salary','uptime'):
                        data[key] = value
            print data
            self.mgr().insert(data)
            name_start += 1

    def generate_player(self, name):
        '''
        通过name在数据库里的数据生成player
        '''
        p = self.find_one({'name':name})
        return p

if __name__ == '__main__':
    MGPlayer.mgr().generate_test_players(26,30,20)









