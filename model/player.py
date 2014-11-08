#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from datetime import date

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

from lib.database import Model

class Player(Model):
    '''
    player
    '''
    def __init__(self):
        self.name = ''
        self.birthdate = ''

        self.position = ''
        self.forward = 0
        self.mid = ''
        self.defence = ''

        self.history_data = None
        self.experience = None



if __name__ == '__main__':
    a = Player()
