#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from datetime import date

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

from lib.database import Model

class PlayerDB(Model):
    '''
    playerDB
    '''
    _db = 'Football'
    _pk = 'id'
    _table = 'player'
    _fields = set(['id','name','birthdate','salary','offensive','defence','dribbling','short_pass','long_pass','finish',
                   'marking','uptime'])
    _scheme = ("`id` BIGINT NOT NULL AUTO_INCREMENT",
		"`name` varchar(64) NOT  NULL DEFAULT ''",
		"`birthdate` datetime NOT NULL DEFAULT '1970-01-01 00:00:00'",
        "`salary` BIGINT NOT NULL DEFAULT '0'",
		"`offensive` BIGINT NOT NULL DEFAULT '0'",
        "`defence` BIGINT NOT NULL DEFAULT '0'",
        "`short_pass` BIGINT NOT NULL DEFAULT '0'",
        "`long_pass` BIGINT NOT NULL DEFAULT '0'",
        "`finish` BIGINT NOT NULL DEFAULT '0'",
        "`marking` BIGINT NOT NULL DEFAULT '0'",
		"`uptime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP",
		"PRIMARY KEY `idx_id` (`id`)",
		"UNIQUE KEY `player_name` (`name`)")




if __name__ == '__main__':
    #PlayerDB.new().init_table()
    pass