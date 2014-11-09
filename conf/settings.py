# -*- coding: utf-8 -*-
# Abstract: settings

import json

# mysql

MYSQLDB = {
	#'host':'192.168.1.108',
	'host':'localhost',
	'port':3306,
	'user':'appleface2050',
    #'user':'appleface',
	'passwd':'root',
	'db':'',
	'sock':''
}

MONGODB = {
    'host':'localhost',
    'user':'',
    'passwd':''
}

DB_CNF = {
	'm':{json.dumps(MYSQLDB):['Football']},
	's':{json.dumps(MYSQLDB):['Football']},
}
















