from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By


class InitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.quit()