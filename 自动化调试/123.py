# coding=gbk
import datetime,xlrd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service(r'd:\driver\chromedriver.exe'))
driver.implicitly_wait(20)
#输入网址
driver.get('https://admin.jushispoc.com/login')
#输入手机号
driver.find_element(By.CSS_SELECTOR,'input[placeholder="请输入手机号"]').send_keys("13520634163")
#输入验证码
driver.find_element(By.CSS_SELECTOR,'input[placeholder="请输入验证码"]').send_keys("911922")
#点击登录
driver.find_element(By.CLASS_NAME,'ivu-btn-long').click()

#选择租户
time.sleep(1)
driver.execute_script("document.getElementsByClassName('chooseInner_btn')[0].click();")

driver.find_element(By.XPATH, '//span[contains(text(),"集团运营工作台")]').click()


driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/ul/div[2]/li/ul/li[10]/span').click()