import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
actionChains = ActionChains(driver)
so = driver.find_element(By.ID,'kw').send_keys('Selenium')
locator = driver.find_element(By.ID,'su')
actionChains.double_click(locator).perform()
time.sleep(6)
driver.quit()