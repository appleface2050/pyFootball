#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

class EventDispatcher():
    def __init__(self):
        self.events = []
        self.finder = Finder()
        self.step1 = Step1()
        self.step2 = Step2()

    def attach_event(self, event_func):
        self.events.append(event_func)

    def attach(self, item):
        self.events.append(item)

    # def detach_event(self):
    #     self.events.pop()

    def notify(self):
        # for fun in self.events:
        #     fun()

        #fun = self.events.pop()
        #fun()

        item = self.events.pop()
        if item == 'step0':
            result = self.finder.run()
        elif item == 'step1':
            result = self.step1.run()
        elif item == 'step2':
            result = self.step2.run()

        if result:
            self.attach(result)

    def start(self):
        while(True):
            if len(self.events)!= 0:
                self.notify()
                time.sleep(1)
            else:
                if self.if_data_exist():
                    self.attach('step0')
                else:
                    print "sleep"
                    time.sleep(1)

    def if_data_exist(self):
        return False

class Finder(object):
    def run(self):
        print "发现数据库存在新数据"
        return "step1"
        #d.attach_event("step0")

class Step1(object):
    def run(self):
        print "step1 start"
        print "step1 finish"
        return "step2"

class Step2(object):
    def run(self):
        print "step2 start"
        print "step2 finish"


if __name__ == '__main__':

    d = EventDispatcher()
    d.attach('step0')
    #d.notify()
    d.start()

