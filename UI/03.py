import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
driver.find_element(By.ID,'kw').send_keys('Selenium')
time.sleep(2)
driver.refresh()
time.sleep(3)
print("测试执行的浏览器：{0}".format(driver.name))
driver.quit()