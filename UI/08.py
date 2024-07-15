import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
actionChains = ActionChains(driver)
so = driver.find_element(By.ID,'kw')
actionChains.context_click(so).perform()
time.sleep(6)
driver.quit()