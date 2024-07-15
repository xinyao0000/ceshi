import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http:www.baidu.com")
time.sleep(2)
driver.get("http:www.bing.com")
time.sleep(2)
driver.back()
print('当前url为：{0}'.format(driver.current_url))
time.sleep(2)
driver.forward()
print('当前url为：{0}'.format(driver.current_url))
driver.quit()