import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
aboutBaiDu = WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'新闻')))
time.sleep(3)
aboutBaiDu.click()
time.sleep(3)
driver.quit()