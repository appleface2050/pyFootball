#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from datetime import date

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

from lib.database import Model



class ClubDB(Model):
    '''
    Club
    '''
    _db = 'Football'
    _pk = 'id'
    _table = 'club'
    _fields = set(['id','name','start','money','league','uptime'])
    _scheme = ("`id` BIGINT NOT NULL AUTO_INCREMENT",
		"`name` varchar(64) NOT  NULL DEFAULT ''",
		"`start` datetime NOT NULL DEFAULT '1970-01-01 00:00:00'",
        "`money` BIGINT NOT NULL DEFAULT '0'",
        "`league` varchar(64) NOT  NULL DEFAULT ''",
		"`uptime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP",
		"PRIMARY KEY `idx_id` (`id`)",
		"UNIQUE KEY `player_name` (`name`)")



if __name__ == '__main__':
    #ClubDB.new().init_table()
    pass