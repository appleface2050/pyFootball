
class TestA(object):

    def deco(func):
        def _deco(a, b):
            assert a in (1,2,3,4)
            ret = func(a, b)
            print a,b
            return ret
        return _deco

    @deco
    def myfunc(self, a, b):
        print(" myfunc(%s,%s) called." % (a, b))
        return a + b
if __name__ == '__main__':
    t = TestA()
    t.myfunc(1, 2)
    t.myfunc(3, 4)


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
