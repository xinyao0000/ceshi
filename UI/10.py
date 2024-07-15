import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
actionChains = ActionChains(driver)
so = driver.find_element(By.ID,'kw')
so.send_keys('Selenium')
time.sleep(3)
so.send_keys(Keys.CONTROL,'a')
time.sleep(3)
so.send_keys(Keys.CONTROL,'c')
time.sleep(3)
so.send_keys(Keys.BACKSPACE)
time.sleep(3)
driver.get("http://www.bing.com")
bingSo = driver.find_element(By.ID,'sb_form_q')
bingSo.send_keys(Keys.CONTROL,'v')
time.sleep(3)
driver.quit()