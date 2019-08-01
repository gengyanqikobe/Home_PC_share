class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)
a = A()
a.foo(5)
a.class_foo(666)
a.static_foo(898)

#https://www.cnblogs.com/elie/p/5876210.html