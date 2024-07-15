import unittest
class BaiDuTest(unittest.TestCase):
    def setUp(self):
        print('start')
    def tearDown(self):
        print('end')
    def test_baidu_so(self):
        print('执行测试用例')

if __name__ == '__main__':
    unittest.main(verbosity=2)