__author__ = 'Xsank'
import inspect
from collections import defaultdict


def add_event(valid_type):
    def decorate(func):
        events = getattr(func, 'events',[])
        events.append(valid_type.id())
        setattr(func,'events',events)
        return func
    return decorate


class Listener(object):
    '''
    This is the base class of all the listeners.
    Your listener have to be inheritanced from it. Otherwise the eventbus
    will throw the ListenertypeError exception when you register it.
    '''
    def __init__(self):
        self.event_handlers=defaultdict(list)
        self.init_event_handlers()

    def init_event_handlers(self):
        for name,func in self.get_handlers():
            for event in func.events:
                self.event_handlers[event].append(func)

    def get_handlers(self):
        funcs=inspect.getmembers(self,predicate=inspect.ismethod)
        return [(name,func) for name,func in funcs if hasattr(func,'events')]