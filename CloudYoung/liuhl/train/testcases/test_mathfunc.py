import unittest
from function.mathfunc import *

class TestMathFunc(unittest.TestCase):
    """Test mathfunc.py"""

    def test_add(self):
        """Test method add(a,b)"""
        print('add')
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        print('minus')
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        print('multi')
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        print('divide')
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMathFunc)
    unittest.TextTestRunner(verbosity=2).run(suite)








    '''延展问题
    1.如果想单独运行或者不运行某个测试case，应该怎么做？
    2.怎样控制每个case的执行顺序
    '''