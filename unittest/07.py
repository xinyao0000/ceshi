from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By


class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.baidu.com")
    def tearDown(self):
        self.driver.quit()
    def test_baidu_news(self):
        self.driver.find_element(By.LINK_TEXT,'新闻').click()
        self.assertEqual(self.driver.current_url,'https://news.baidu.com/')
    def test_baidu_map(self):
        self.driver.find_element(By.LINK_TEXT,'地图').click()
        self.assertEqual(self.driver.current_url,'https://map.baidu.com/')
    @staticmethod
    def suite(testCaseClass):
        suite = unittest.TestLoader().loadTestsFromTestCase(testCaseClass)
        return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(BaiduTest.suite(BaiduTest))