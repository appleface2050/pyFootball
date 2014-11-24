#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 观察者模式，调用函数

class Subject(object):
    '''
    abstract class
    '''
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.pop(observer)

    def notify(self):
        for o in self.observers:
            o.update()

class Secretary(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.action = "boss come back"

class Boss(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.update_func = []
        self.action = "fresh meet !!!"

    def add_event(self, event):
        self.update_func.append(event)

    def notify(self):
        for fun in self.update_func:
            fun()

class Observer(object):
    '''
    abstract class
    '''
    def __init__(self, name, secretary):
        self.name = name
        self.secretary = secretary

    def update(self):
        pass

class StockObserver(Observer):
    def __init__(self, name, secretary):
        Observer.__init__(self,name,secretary)

    def update(self):
        print "%s, %s, do not watch stock" % (self.secretary.action,self.name)

    def close_stock(self):
        print "%s, %s, do not watch stock, hurry up" % (self.secretary.action,self.name)

class NBAObserver(Observer):
    def __init__(self, name, secretary ):
        Observer.__init__(self,name,secretary)

    def update(self):
        print "%s, %s, do not watch NBA" % (self.secretary.action,self.name)

if __name__ == '__main__':
    secretary = Secretary()
    stock_ob1 = StockObserver('张三',secretary)
    nba_ob1 = StockObserver('王五',secretary)
    secretary.attach(stock_ob1)
    secretary.attach(nba_ob1)
    secretary.notify()

    boss = Boss()
    stock_ob2 = StockObserver('李四',boss)
    boss.add_event(stock_ob2.close_stock)
    boss.notify()



