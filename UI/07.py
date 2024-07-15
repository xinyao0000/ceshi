import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
actionChains = ActionChains(driver)
locater = driver.find_element(By.CSS_SELECTOR,'#s-usersetting-top')
actionChains.move_to_element(locater).perform()
driver.find_element(By.XPATH,'//*[@id="s-user-setting-menu"]/div/a[1]/span').click()
time.sleep(3)
driver.quit()