from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By


class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.baidu.com")
    def test_title(self):
        self.assertEqual(self.driver.title,'百度一下，你就知道')
    def test_so(self):
        so = self.driver.find_element(By.ID,'kw')
        self.assertTrue(so.is_enabled())
    def test_002(self):
        self.driver.find_element(By.LINK_TEXT,'新闻').click()
    @unittest.skip('do not run')
    def test_003(self):
        self.driver.find_element(By.LINK_TEXT,'地图').click()
    def tearDown(self):
        self.driver.quit()

class BaiduMap(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.quit()
    def test_baidu_map(self):
        self.driver.find_element(By.LINK_TEXT,'地图').click()
        self.driver.get('http://www.baidu.com')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule('06.py')
    unittest.TextTestRunner(verbosity=2).run(suite)