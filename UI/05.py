import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://mail.sina.com/#")
driver.find_element(By.ID,'freename').send_keys('')
driver.find_element(By.ID,'freepassword').send_keys('')
driver.find_element(By.LINK_TEXT,'登录').click()
WebDriverWait(driver,10).until(expected_conditions.text_to_be_present_in_element((By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]'),'请输入邮箱名'))
print("打印结果：{0}".format(list))
time.sleep(3)
driver.quit()