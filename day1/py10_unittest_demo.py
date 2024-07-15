import unittest

def add(x,y):
    return x + y

class TestAdd(unittest.TestCase):

    def setUp(self) -> None:
        print("----------setUp--------------")

    def tearDown(self) -> None:
        print("----tearDown-----")

    @classmethod
    def setUpClass(cls) -> None:
        print("----------setUpClass--------------")

    @classmethod
    def tearDownClass(cls) -> None:
        print("----------tearDownClass--------------")

    def test01_add(self):
        print("测试方法1")
        ret = add(10,20)
        self.assertEqual(30,ret)

    def test02_add(self):
        print("测试方法2")
        ret = add(100,200)
        self.assertEqual(300,ret)

