import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
actionChains = ActionChains(driver)
driver.find_element(By.ID,'kw').send_keys('Selenium')
driver.find_element(By.ID,'su').click()
down = "var q = document.documentElement.scrollTop = 10000"
time.sleep(6)
driver.execute_script(down)
time.sleep(3)
driver.find_element(By.LINK_TEXT,'下一页 >').click()
time.sleep(3)
up = "var q = document.documentElement.scrollTop = 0"
driver.execute_script(down)
time.sleep(3)
driver.execute_script(up)
time.sleep(4)
driver.quit()