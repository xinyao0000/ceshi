import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SinaTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://mail.sina.com.cn/")
        self.driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.quit()
    def test_username_password_null(self):
        self.driver.find_element(By.ID,'freename').send_keys('')
        self.driver.find_element(By.ID,'freepassword').send_keys('')
        self.driver.find_element(By.LINK_TEXT,'登录').click()
        divError = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
        self.assertEqual(divError,'请输入邮箱名')

if __name__ == '__main__':
    unittest.main(verbosity=2)