import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By


class BaiduTest(unittest.TestCase):

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
        url = self.driver.current_url
        self.assertEqual(url,'https://news.baidu.com/')
    def test_baidu_map(self):
        self.driver.find_element(By.LINK_TEXT,'地图')
        self.driver.get('http://www.baidu.com')

# if __name__ == '__main__':
# #     suite = unittest.TestSuite()
# #     suite.addTest(BaiduTest('test_baidu_news'))
# #     suite.addTest(BaiduTest('test_baidu_map'))
# #     unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BaiduTest)
    unittest.TextTestRunner(verbosity=2).run(suite)