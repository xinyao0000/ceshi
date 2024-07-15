import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://mail.sina.com.cn/")
driver.implicitly_wait(30)
now_handle = driver.current_window_handle
time.sleep(2)
driver.find_element(By.LINK_TEXT,'注册').click()
time.sleep(2)
handles = driver.window_handles
for handle in handles:
    if handle!= now_handle:
        driver.switch_to.window(handle)
        time.sleep(2)
        driver.find_element(By.NAME,'email').send_keys('wuya')
        time.sleep(2)
        driver.close()
driver.switch_to.window(now_handle)
time.sleep(3)
driver.find_element(By.ID,'freename').send_keys('wuya')
time.sleep(4)
driver.quit()