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



# <editor-fold desc="ȫ��">

# </editor-fold>
class test_01CreatOrder(unittest.TestCase):


  # <editor-fold desc="����">
  def GetPhoneNum(self):
    seed = "1234567890"
    sa = []
    for i in range(9):
      sa.append(random.choice(seed))
    phoneNum = '13' + ''.join(sa)
    return  phoneNum

  # </editor-fold>

  # <editor-fold desc="�о�">
  @classmethod
  def setUpClass(cls):
      book = xlrd.open_workbook(r'E:/data/webpay_date.xlsx')
      date = book.sheet_by_index(0)
      dateList = date.row_values(1)
      # ��ֵ
      cls.className = str(dateList[0]).strip('\r\n\t')
      cls.loginNum = str(dateList[1]).strip('\r\n\t')
      cls.name = str(dateList[2]).strip('\r\n\t')
      cls.addr = str(dateList[3]).strip('\r\n\t')
      if len(cls.loginNum) == 0:
          cls.loginNum = 0
      else:
          cls.loginNum = int(dateList[1])
      if str(dateList[4]).strip('\r\n\t') == '��':
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

  # <editor-fold desc="����">
  def test01_login(self):
      self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div/div[2]/div[2]/div/div/div[2]').click()

      # ������¼�˺�
      if self.loginNum == 0:
          loginNum = self.GetPhoneNum()
          self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='�������ֻ���']").send_keys(loginNum)
          globals()['loginNum'] = loginNum
      else:
          self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='�������ֻ���']").send_keys(self.loginNum)

      self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='��������֤��']").send_keys('911106')
      self.driver.find_element(By.CSS_SELECTOR, "button[class='el-button el-button--default login']").click()

      self.assertTrue(self.driver.find_element(By.CSS_SELECTOR,"button[class='el-button tx el-button--primary el-dropdown-selfdefine']"))

  def test02_getClass(self):
      self.driver.find_elements(By.CSS_SELECTOR, "div[class='nav_item']")[0].click()
      time.sleep(1)
      self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="����ؼ��������γ�"]').send_keys(self.className)
      self.driver.find_element(By.CSS_SELECTOR, 'button[class ="el-button el-button--default"]').click()


      count = self.driver.find_elements(By.CSS_SELECTOR,"div[class='courseitem']").count
      print(count)
      self.assertEqual(count,1)

      #�ж��������

  def test03_toSignUp(self):
      self.driver.find_element(By.XPATH, '// *[ @ id = "app"] / div[2] / div[3] / div / div').click()
      time.sleep(1)
      self.driver.find_element(By.XPATH, '//span[contains(text(),"���̱���")]').click()

      time.sleep(1)
      if self.driver.find_elements(By.CSS_SELECTOR, 'div[class="placeorder_main_title"]>span')[3].text == '����ջ���Ϣ':
          IsAddr = True
          globals()['isAddr'] = IsAddr
      else:
          IsAddr = False
          globals()['isAddr'] = IsAddr

      print(self.driver.find_elements(By.CSS_SELECTOR, 'div[class="placeorder_main_title"]>span')[3].text)
      print(globals()['isAddr'])

  def test04_importConsignee(self):
      if globals()['isAddr'] == True:
          self.driver.find_element(By.XPATH, '//span[contains(text(),"����ջ���Ϣ")]').click()
          time.sleep(0.5)
          self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="����д�ջ�������"]').send_keys(self.name)
          select1 = Select(self.driver.find_elements(By.CSS_SELECTOR, "div[class='distpicker-address-wrapper']>select")[0])
          select1.select_by_visible_text('������')
          time.sleep(0.5)
          select2 = Select(self.driver.find_elements(By.CSS_SELECTOR, "div[class='distpicker-address-wrapper']>select")[1])
          select2.select_by_visible_text('������')
          time.sleep(0.5)
          select3 = Select(self.driver.find_elements(By.CSS_SELECTOR, "div[class='distpicker-address-wrapper']>select")[2])
          select3.select_by_visible_text('��̨��')
          time.sleep(0.5)
          self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="����д��ϸ��ַ"]').send_keys(self.addr)
          self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="����д�ջ��˵绰"]').send_keys(globals()['loginNum'])
          self.driver.find_element(By.CSS_SELECTOR, "div[class='save_btu']").click()

      self.assertTrue(self.driver.find_elements(By.CSS_SELECTOR, 'div[class="placeorder_main_title"]>span')[3].text != '����ջ���Ϣ')

  def test05_subOrder(self):
      self.driver.find_element(By.CSS_SELECTOR, "div[class='placeorder_submit']").click()
      time.sleep(5)
      self.driver.find_element(By.XPATH, '//span[contains(text(),"ͬ�Ȿ����,����֧��")]').click()
      time.sleep(0.5)
      self.driver.find_element(By.CSS_SELECTOR, "div[class='placeorder_submit']").click()
      time.sleep(3)
      self.assertTrue(self.driver.find_element(By.ID,'J_qrPayArea'))

  def test06_screenshots(self):
      self.driver.save_screenshot(r"E:\\autoTest\printscreen\pay.png")
      scrEnd = subprocess.getoutput("dir e:\printscreen\pay.png /s/b")
      # self.assertIn('e:\autoTest\printscreen\pay.png', scrEnd, 'δ�ҵ���ͼ')
      self.assertNotIn('�Ҳ����ļ�', scrEnd, 'δ�ҵ���ͼ')

  # </editor-fold>

if __name__ == '__main__':
    unittest.main()










