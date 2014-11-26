#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import datetime

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

from lib.mongodb import MGModel

class MGClub(MGModel):
    '''
    MONGO club
    '''
    _db = 'fb'
    _collection = 'club'

    def get_all_club_data(self):
        return self.mgr().find_all()
