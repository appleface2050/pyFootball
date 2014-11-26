# -*- coding: utf-8 -*-
# Abstract: settings

import json

# mysql

MYSQLDB = {
	#'host':'192.168.1.108',
	'host':'192.168.60.130',
	'port':3306,
	'user':'root',
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
	'm':{json.dumps(MYSQLDB):['fb']},
	's':{json.dumps(MYSQLDB):['fb']},
}

DB_LOCALHOST = {'host':'localhost',
             'port':27017,
             'user':'',
             'passwd':''}














