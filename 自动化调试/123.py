# coding=gbk
import datetime,xlrd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service(r'd:\driver\chromedriver.exe'))
driver.implicitly_wait(20)
#������ַ
driver.get('https://admin.jushispoc.com/login')
#�����ֻ���
driver.find_element(By.CSS_SELECTOR,'input[placeholder="�������ֻ���"]').send_keys("13520634163")
#������֤��
driver.find_element(By.CSS_SELECTOR,'input[placeholder="��������֤��"]').send_keys("911922")
#�����¼
driver.find_element(By.CLASS_NAME,'ivu-btn-long').click()

#ѡ���⻧
time.sleep(1)
driver.execute_script("document.getElementsByClassName('chooseInner_btn')[0].click();")

driver.find_element(By.XPATH, '//span[contains(text(),"������Ӫ����̨")]').click()


driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/ul/div[2]/li/ul/li[10]/span').click()