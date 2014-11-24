#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

class Observer(object):
    '''
    abstract class
    '''
    def update(self):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.subjectState = ''

    def get_subject_state(self):
        return self.subjectState

    def set_sebject_state(self, state):
        self.subjectState = state

class ConcreteObserver(Observer):
    def __init__(self, concrete_subject, name ):
        Observer.__init__(self)
        self.observerState = ''
        self.name = name
        self.concrete_subject = concrete_subject

    def get_subject(self):
        return self.concrete_subject

    def set_subject(self, subject):
        self.concrete_subject = subject

    def update(self):
        '''
        override
        '''
        self.observerState = self.get_subject().get_subject_state()
        print "The observer's state of %s is %s"% (self.name, self.observerState)

if __name__ == '__main__':
    a = ConcreteSubject()
    o1 = ConcreteObserver(a,"Observer1")
    o2 = ConcreteObserver(a,"Observer2")
    o3 = ConcreteObserver(a,"Observer3")

    a.attach(o1)
    a.attach(o2)
    a.attach(o3)
    a.set_sebject_state("Ready")
    a.notify()




