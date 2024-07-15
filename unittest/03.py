from selenium import webdriver
import unittest

class UiTset(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start')

    @classmethod
    def tearDownClass(cls):
        print('end')

    def test_01(self):
        print('第一个')

    def test_02(self):
        print('第二个')

if __name__ == '__main__':
    unittest.main()
