#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TestA(object):
    def deco(func):
        def _deco(self, a, b):
            print a,b
            func(self, a, b)
        return _deco

    @deco
    def myfunc(self, a, b):
        print(" myfunc(%s,%s) called." % (a, b))

if __name__ == '__main__':
    t = TestA()
    t.myfunc(1, 2)



# def deco(func):
#     def _deco(a, b):
#         assert a in (1,2,3,4)
#         ret = func(a, b)
#         print a,b
#         return ret
#     return _deco
#
# @deco
# def myfunc(a, b):
#     print(" myfunc(%s,%s) called." % (a, b))
#     return a + b
