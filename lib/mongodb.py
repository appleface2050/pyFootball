#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo,os,sys

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

from conf.settings import DB_MUSICMAGV2

class Mongo(object):
    def __init__(self, db_conf=DB_MUSICMAGV2):
        '''
        Mongodb Wrapper
        '''
        self.db_conf = db_conf
        self.conn = None
        self.db = None
        self.collection = None
        #self.curdb = ""
        self.connect(self.db_conf)

    def __del__(self):
        self.close()

    def __repr__(self):
        return "Mongodb(%s)"%(str(self.db_conf),)

    def __str__(self):
        return "Mongodb(%s)"%(str(self.db_conf),)

    def connect(self, db_conf):
        """
        connect to Mongodb server
        """
        self.conn = pymongo.Connection(db_conf['host'],db_conf['port'])
        return True

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

class Model(object):
    '''
    Collection
    '''
    _db = ""
    _collection = ""
    _fields = set()
    _mongo = None

    def __init__(self):
        self.cursor = None
        self._mongo = Mongo()
        self.db = self._mongo.conn[self._db]
        self.collection = self.db[self._collection]

    @property
    def _clc(self):
        return self.collection

    def find_all(self):
        self.cursor = self.find()
        return self.cursor

    @classmethod
    def mgr(cls, **kargs):
        return cls(**kargs)

    def insert(self, doc_or_docs, manipulate=True,
               safe=None, check_keys=True, continue_on_error=False, **kwargs):
        return self._clc.insert(doc_or_docs, manipulate,safe, check_keys, continue_on_error, **kwargs)

    def find(self, statement=None):
        if statement:
            return self._clc.find(statement)
        else:
            return self._clc.find()

    def truncate_collection(self):
        pass

    def drop(self):
        return self._clc.drop()

    # def remove(self, spec_or_id=None, safe=None, multi=True, **kwargs):
    #     return self._clc.remove(spec_or_id,safe,multi,**kwargs)

    #for centos /usr/lib64/python2.6/site-packages/pymongo/collection.py
    def remove(self, spec_or_id=None, safe=None, **kwargs):
        return self._clc.remove(spec_or_id,safe,**kwargs)

    def find_one(self, spec_or_id=None, *args, **kwargs):
        return  self._clc.find_one(spec_or_id,*args, **kwargs)

    def create_index(self, key_or_list, cache_for, **kwargs):
        return self._clc.create_index(key_or_list,cache_for,**kwargs)

    def ensure_index(self, key_or_list, cache_for, **kwargs):
        return self._clc.ensure_index(key_or_list,cache_for,**kwargs)

    def drop_index(self, index_or_name):
        return self._clc.drop_index(index_or_name)

    def drop_indexes(self):
        return self._clc.drop_indexes()

    def index_information(self):
        return self._clc.index_information()

    def rename(self, new_name, **kwargs):
        return self._clc.rename(new_name, **kwargs)

    def distinct(self, key):
        return self._clc.distinct(key)

    def update(self, spec, document, upsert=False, manipulate=False,
               safe=None, multi=False, check_keys=True, **kwargs):
        return self._clc.update(spec,document,upsert,manipulate,safe,multi,check_keys,**kwargs)