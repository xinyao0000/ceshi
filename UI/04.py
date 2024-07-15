import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
so = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.ID,'kw')))
so.send_keys('Selenium')
time.sleep(10)
driver.quit()