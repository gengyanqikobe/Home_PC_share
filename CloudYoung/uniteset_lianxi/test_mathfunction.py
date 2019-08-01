import unittest
from uniteset_lianxi.mathfunction import  *




class TestMathFuncion(unittest.TestCase):
    def setUp(self):
        print("do something before test_t")
    def tearDown(self):
        print("do something after test_t")

    def test_add(self):
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(4,add(1,2))

    def test_sub(self):
        self.assertEqual(1,sub(5,4))

    @unittest.skip("test_mul was passed")

    def test_mul(self):
        self.assertEqual(6,mul(2,3))

    def test_div(self):
        self.assertEqual(2.5,div(5,1))

if __name__ =='__main__':
    unittest.main()