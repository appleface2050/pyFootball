#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Queue import Queue
import time

class A(object):
    def __init__(self):
        self.q = Queue(10)

    def func1(self):
        print "func1"
        self.cal_2()

    def func2(self):
        print "func2"
        self.cal_1()

    def cal_1(self):
        self.q.put("1")

    def cal_2(self):
        self.q.put("2")

    def go(self):
        while(True):
            if not self.q.empty():
                #print self.q.qsize()
                item = self.q.get()
                if item == '1':
                    self.func1()
                elif item == '2':
                    self.func2()
            else:
                print "sleep 1"
                time.sleep(1)

if __name__ == '__main__':
    a = A()
    a.cal_1()
    a.cal_2()

    a.go()
