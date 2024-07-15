import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By


class test_BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        self.driver.find_element(By.LINK_TEXT,'新闻').click()
        time.sleep(3)
    def test_baidu_news(self):
        self.driver.find_element(By.LINK_TEXT,'地图').click()
        time.sleep(3)
if __name__ == '__main__':
    unittest.main(verbosity=2)