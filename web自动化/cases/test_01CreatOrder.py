# coding=gbk
import os.path
import random,time
import unittest
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import subprocess



# <editor-fold desc="全局">

# </editor-fold>
class test_01CreatOrder(unittest.TestCase):


  # <editor-fold desc="工具">
  def GetPhoneNum(self):
    seed = "1234567890"
    sa = []
    for i in range(9):
      sa.append(random.choice(seed))
    phoneNum = '13' + ''.join(sa)
    return  phoneNum

  # </editor-fold>

  # <editor-fold desc="夹具">
  @classmethod
  def setUpClass(cls):
      book = xlrd.open_workbook(r'E:/data/webpay_date.xlsx')
      date = book.sheet_by_index(0)
      dateList = date.row_values(1)
      # 赋值
      cls.className = str(dateList[0]).strip('\r\n\t')
      cls.loginNum = str(dateList[1]).strip('\r\n\t')
      cls.name = str(dateList[2]).strip('\r\n\t')
      cls.addr = str(dateList[3]).strip('\r\n\t')
      if len(cls.loginNum) == 0:
          cls.loginNum = 0
      else:
          cls.loginNum = int(dateList[1])
      if str(dateList[4]).strip('\r\n\t') == '是':
          cls.isPay = True
      else:
          cls.isPay = False

      globals()['isPay'] = cls.isPay

      cls.driver = webdriver.Chrome(service=Service(r'd:\driver\chromedriver.exe'))
      cls.driver.implicitly_wait(30)

      cls.driver.get('https://www.jushispoc.com/#/home')
      cls.driver.maximize_window()
  @classmethod
  def tearDownClass(cls):
    time.sleep(1)
    if globals()['isPay']:
        os.system('python test_02PayByPhone.py')

  def setUp(self):
    time.sleep(2)

  def tearDown(self):
    pass

  # </editor-fold>

  # <editor-fold desc="用例">
  def test01_login(self):
      self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div/div[2]/div[2]/div/div/div[2]').click()

      # 构建登录账号
      if self.loginNum == 0:
          loginNum = self.GetPhoneNum()
          self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='请输入手机号']").send_keys(loginNum)
          globals()['loginNum'] = loginNum
      else:
          self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='请输入手机号']").send_keys(self.loginNum)

      self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='请输入验证码']").send_keys('911106')
      self.driver.find_element(By.CSS_SELECTOR, "button[class='el-button el-button--default login']").click()

      self.assertTrue(self.driver.find_element(By.CSS_SELECTOR,"button[class='el-button tx el-button--primary el-dropdown-selfdefine']"))

  def test02_getClass(self):
      self.driver.find_elements(By.CSS_SELECTOR, "div[class='nav_item']")[0].click()
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="输入关键词搜索课程"]').send_keys(self.className)
      self.driver.find_element(By.CSS_SELECTOR, 'button[class ="el-button el-button--default"]').click()


      count = self.driver.find_elements(By.CSS_SELECTOR,"div[class='courseitem']").count
      print(count)
      self.assertEqual(count,1)

      #判断搜索结果

  def test03_toSignUp(self):
      self.driver.find_element(By.XPATH, '// *[ @ id = "app"] / div[2] / div[3] / div / div').click()
      time.sleep(1)
      self.driver.find_element(By.XPATH, '//span[contains(text(),"立刻报名")]').click()

      time.sleep(1)
      if self.driver.find_elements(By.CSS_SELECTOR, 'div[class="placeorder_main_title"]>span')[3].text == '添加收货信息':
          IsAddr = True
          globals()['isAddr'] = IsAddr
      else:
          IsAddr = False
          globals()['isAddr'] = IsAddr

      print(self.driver.find_elements(By.CSS_SELECTOR, 'div[class="placeorder_main_title"]>span')[3].text)
      print(globals()['isAddr'])

  def test04_importConsignee(self):
      if globals()['isAddr'] == True:
          self.driver.find_element(By.XPATH, '//span[contains(text(),"添加收货信息")]').click()
          time.sleep(0.5)
          self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请填写收货人姓名"]').send_keys(self.name)
          select1 = Select(self.driver.find_elements(By.CSS_SELECTOR, "div[class='distpicker-address-wrapper']>select")[0])
          select1.select_by_visible_text('北京市')
          time.sleep(0.5)
          select2 = Select(self.driver.find_elements(By.CSS_SELECTOR, "div[class='distpicker-address-wrapper']>select")[1])
          select2.select_by_visible_text('北京市')
          time.sleep(0.5)
          select3 = Select(self.driver.find_elements(By.CSS_SELECTOR, "div[class='distpicker-address-wrapper']>select")[2])
          select3.select_by_visible_text('丰台区')
          time.sleep(0.5)
          self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请填写详细地址"]').send_keys(self.addr)
          self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请填写收货人电话"]').send_keys(globals()['loginNum'])
          self.driver.find_element(By.CSS_SELECTOR, "div[class='save_btu']").click()

      self.assertTrue(self.driver.find_elements(By.CSS_SELECTOR, 'div[class="placeorder_main_title"]>span')[3].text != '添加收货信息')

  def test05_subOrder(self):
      self.driver.find_element(By.CSS_SELECTOR, "div[class='placeorder_submit']").click()
      time.sleep(5)
      self.driver.find_element(By.XPATH, '//span[contains(text(),"同意本条款,继续支付")]').click()
      time.sleep(0.5)
      self.driver.find_element(By.CSS_SELECTOR, "div[class='placeorder_submit']").click()
      time.sleep(3)
      self.assertTrue(self.driver.find_element(By.ID,'J_qrPayArea'))

  def test06_screenshots(self):
      self.driver.save_screenshot(r"E:\\autoTest\printscreen\pay.png")
      scrEnd = subprocess.getoutput("dir e:\printscreen\pay.png /s/b")
      # self.assertIn('e:\autoTest\printscreen\pay.png', scrEnd, '未找到截图')
      self.assertNotIn('找不到文件', scrEnd, '未找到截图')

  # </editor-fold>

if __name__ == '__main__':
    unittest.main()










