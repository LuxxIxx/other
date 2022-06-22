# coding=gbk
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
import time,os
import unittest

desired_caps = {
  'platformName': 'Android',
  'platformVersion': '10',
  'deviceName': 'Mi 10',
  'appPackage': 'com.eg.android.AlipayGphone',
  'appActivity': '.AlipayLogin',
  'unicodeKeyboard': True, # �����ַ�ʱʹ�õ����뷨
  'resetKeyboard': True,
   'noReset': True,       # ��Ҫ����App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}

class test_PayByPhone(unittest.TestCase):

  # <editor-fold desc="����">
  def getalbumPos(self):
      x = int(0.86759 * self.driver.get_window_size()['width'])
      y = int(0.86355 * self.driver.get_window_size()['height'])
      return (x, y)

  def getPasswordPos(self,password):
      return [525,1676,525,1676,525,1676,886,1676,886,1676,886,1676]
  # �����ߴ�1080 2206
  # </editor-fold>

  # <editor-fold desc="�о�">
  @classmethod
  def setUpClass(cls):
      cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
      cls.driver.implicitly_wait(8)
      cls.driver.password = 123456

  @classmethod
  def tearDownClass(cls):
    cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    cls.driver.save_screenshot('./images/payByPhone/end.png')
  def setUp(self):
    time.sleep(1)
  def tearDown(self):
      pass

  # </editor-fold>

  # <editor-fold desc="����">
  def test01_sendPic(self):
      os.system('adb push E:/autoTest/printscreen/pay.png /sdcard/1/pay.png')

  def test02_goAlbum(self):
      self.driver.find_element(AppiumBy.ID, "com.alipay.android.phone.openplatform:id/icon_container").click()
      self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='ɨһɨ']").click()
      self.driver.tap([self.getalbumPos()])
      self.driver.find_element(AppiumBy.ID, "com.alipay.mobile.beephoto:id/tv_go_system_select").click()

  def test03_chooseApply(self):
      self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='�ļ�����']").click()

  def test04_chooseFile(self):
      self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='1']").click()
      self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='pay.png']").click()
      self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='ȷ��']").click()

  def test05_enterPassword(self):
      self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ʹ������")').click()
      time.sleep(1)
      self.driver.tap(self.getPasswordPos(self.getPasswordPos(self.password)[0]), self.getPasswordPos(self.getPasswordPos(self.password)[1]))
      time.sleep(0.2)
      self.driver.tap(self.getPasswordPos(self.getPasswordPos(self.password)[2]), self.getPasswordPos(self.getPasswordPos(self.password)[3]))
      time.sleep(0.2)
      self.driver.tap(self.getPasswordPos(self.getPasswordPos(self.password)[4]), self.getPasswordPos(self.getPasswordPos(self.password)[5]))
      time.sleep(0.2)
      self.driver.tap(self.getPasswordPos(self.getPasswordPos(self.password)[6]), self.getPasswordPos(self.getPasswordPos(self.password)[7]))
      time.sleep(0.2)
      self.driver.tap(self.getPasswordPos(self.getPasswordPos(self.password)[8]), self.getPasswordPos(self.getPasswordPos(self.password)[9]))
      time.sleep(0.2)
      self.driver.tap(self.getPasswordPos(self.getPasswordPos(self.password)[10]), self.getPasswordPos(self.getPasswordPos(self.password)[11]))
  # </editor-fold>


if __name__ == '__main__':
    testcases = unittest.TestLoader().loadTestsFromTestCase(test_PayByPhone)
    with open('../report/payReport02.txt', "w+") as txtfile:
        unittest.TextTestRunner(stream=txtfile, verbosity=2).run(testcases)
    unittest.main()





