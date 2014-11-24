class EventDispatcher(object):
    def __init__(self):
        self.events = {}
    def addEventListener(self,eventType,listenFunction):
        if not self.events.has_key(eventType):
            self.events[eventType] = []
        eventList = self.events[eventType]
        eventList.append(listenFunction)

    def removeEventListener(self,eventType,ListenFunction):
        if not self.events.has_key(eventType):
            return
        eventList = self.events[eventType]
        eventList.remove(ListenFunction)

    def dispatchEvent(self,event):
        if not self.events.has_key(event.type):
            return
        
        eventList = self.events[event.type]
        for fun in eventList:
            fun()


class Aevent(object):
    def __init__(self,Type):
        self.type = Type

class Obj(EventDispatcher):
    def __init__(self):
        EventDispatcher.__init__(self)
        self.i = 1

    def addI(self):
        self.i += 1
        aevent = Aevent('iadd')
        self.dispatchEvent(aevent)

def onIadd():
    print o.i

o = Obj()
o.addEventListener('iadd',onIadd)
o.addI()    #output 2
o.addI()    #output 3
o.removeEventListener('iadd',onIadd)
o.addI()    #output 3