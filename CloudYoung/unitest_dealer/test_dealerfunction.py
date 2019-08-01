from unitest_dealer.dealerfunction import login
import unittest

class TestDealerFunction(unittest.TestCase):
    """这是登录接口"""

    def test_login(self):
        self.assertEqual('true',login(10001,123456))#正确用户名密码
        self.assertNotEqual('true',login(11111,11111))#错误用户名密码
        self.assertEqual('true',login('10001',123456))
        self.assertNotEqual('true',login(11111,''))

if __name__ == '__main__':
    unittest.main()