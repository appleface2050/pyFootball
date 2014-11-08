#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from datetime import date

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

from lib.database import Model



class Club(Model):
    '''
    Club
    '''