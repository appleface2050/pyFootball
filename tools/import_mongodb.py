#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from datetime import date
from model.mgclub import MGClub
from model.mgplayer import MGPlayer

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))



file_club_tab = "E:\\dev document\\pyFootball\\mongodb_data\\club_tab.txt"
file_player_tab = "E:\\dev document\\pyFootball\\mongodb_data\\player_tab.txt"

f = open(file_club_tab,'r')
lines = f.readlines()
data = {}
for line in lines[1:]:
    tmp = line.strip().split('\t')
    data['uptime'] = tmp[1]
    data['name'] = tmp[2]
    data['money'] = tmp[3]
    data['league'] = tmp[4]
    data['club_name'] = tmp[5]
    print data
    MGClub.mgr().insert(data)