from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
import time,os
from web支付_创建订单 import webPay


desired_caps = {
  'platformName': 'Android',
  'platformVersion': '10',
  'deviceName': 'Mi 10',
  'appPackage': 'com.eg.android.AlipayGphone',
  'appActivity': '.AlipayLogin',
  'unicodeKeyboard': True, # 特殊字符时使用的输入法
  'resetKeyboard': True,
   'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}

#开发尺寸1080 2206
def getalbumPos():
  x = int(0.86759*driver.get_window_size()['width'])
  y = int(0.86355*driver.get_window_size()['height'])
  return (x,y)

def payByPhone():
  os.system('adb push E:/printscreen/pay.png /sdcard/1/pay.png')
  print(1)

  driver.find_element(AppiumBy.ID,"com.alipay.android.phone.openplatform:id/icon_container").click()
  driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='扫一扫']").click()
  driver.tap([getalbumPos()])
  # driver.find_element(AppiumBy.ID, "com.alipay.mobile.scan:id/title_bar_album").click()
  driver.find_element(AppiumBy.ID, "com.alipay.mobile.beephoto:id/tv_go_system_select").click()

  if driver.find_element(AppiumBy.ID,'miui:id/parentPanel'):
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='文件管理']").click()

  driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='1']").click()
  driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='pay.png']").click()
  time.sleep(0.5)
  driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='确定']").click()

  if Data.isPay == True:
    # 输入密码
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("使用密码")').click()
    time.sleep(1)
    driver.tap(525, 1676)
    time.sleep(0.2)
    driver.tap(525, 1676)
    time.sleep(0.2)
    driver.tap(525, 1676)
    time.sleep(0.2)
    driver.tap(886, 1676)
    time.sleep(0.2)
    driver.tap(886, 1676)
    time.sleep(0.2)
    driver.tap(886, 1676)

if __name__ == '__main__':
  driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
  driver.implicitly_wait(8)
  Data = webPay()
  try:
    payByPhone()
    print('成功')
  except:
    print('失败')
