from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By


class BaiDuTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://www.baidu.com")
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element(By.LINK_TEXT,'新闻').click()
        self.driver.get("http://www.baidu.com")

    def test_baidu_map(self):
        self.driver.find_element(By.LINK_TEXT,'地图').click()
        self.driver.get("http://www.baidu.com")

if __name__ == '__main__':
    unittest.main()