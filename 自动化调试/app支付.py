import random,time,os
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.webdriver.common.appiumby import AppiumBy

def getSize(x1,y1):
  x_1 = x1/1080
  y_1 = y1/2206
  x = driver.get_window_size()['width']
  y = driver.get_window_size()['height']
  return (x * x_1, y * y_1)

desired_caps = {
  'platformName': 'Android',
  'platformVersion': '10',
  'deviceName': 'Mi 10',
  'appPackage': 'com.jushispoc.JswApp',
  'appActivity': '.activitys.LoadingActivity',
  'unicodeKeyboard': True, # 特殊字符时使用的输入法
  'resetKeyboard': True,
  # 'noReset': false,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(8)
# 如果有`协议弹窗`界面，点击`同意`
protocol = driver.find_element(AppiumBy.ID, "popLl")
if protocol:
    driver.find_element(AppiumBy.ID, "rightTv").click()

driver.implicitly_wait(1)

ll_parent = driver.find_element(AppiumBy.ID, "ll_parent")
if ll_parent:
    driver.find_element(AppiumBy.ID, "rightTv").click()

# 定位输入框
seed = "1234567890"
sa = []
for i in range(9):
  sa.append(random.choice(seed))
phoneNum = ''.join(sa)
sbox = driver.find_element(AppiumBy.ID, 'phoneEt')
sbox.send_keys('13'+phoneNum)

# 确定登录 关闭验证
enter = driver.find_element(AppiumBy.ID,'loginTv').click()
time.sleep(3)
driver.tap([getSize(958,759)])

# 输入验证码
# driver.find_element(AppiumBy.ID, 'codeEt').click()
driver.find_element(AppiumBy.ID, 'codeEt').send_keys('911106')

#选择考试目标
driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.RelativeLayout")[0].click()

#朕知道了
know = driver.find_element(AppiumBy.ID, "mainGuideSureIv")
if know:
    driver.find_element(AppiumBy.ID, "mainGuideSureIv").click()

# 广告弹窗
allLl = driver.find_element(AppiumBy.ID, "allLl")
if allLl:
    driver.find_element(AppiumBy.ID, "closeIv").click()

# 进入课程班级
time.sleep(1)
driver.tap([getSize(400,800)])
# 选择购买班级
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("一级班 幼儿")').click()

#立刻报名
driver.find_element(AppiumBy.ID, "laytouDefultState").click()
driver.find_element(AppiumBy.ID, "sendTv").click()

# 提交订单
driver.find_element(AppiumBy.ID, "rl_address").click()

#输入地址信息
driver.find_element(AppiumBy.ID, 'et_name').send_keys('测试人员')
driver.find_element(AppiumBy.ID, 'et_phone').send_keys('13000000001')
driver.find_element(AppiumBy.ID, "ll_address").click()
driver.find_element(AppiumBy.ID, "btnSubmit").click()
driver.find_element(AppiumBy.ID, 'et_address').send_keys('测试地址')
driver.find_element(AppiumBy.ID, "tv_commit").click()

# 同意协议
driver.find_element(AppiumBy.ID, "cb_order").click()
#权限
try:
  time.sleep(5)
  driver.find_element(AppiumBy.ID, "tvSubmit").click()
except:
  time.sleep(1)
  driver.tap([getSize(530, 2160)])
  time.sleep(5)
  driver.find_element(AppiumBy.ID, "tvSubmit").click()


# 跳转支付
driver.find_element(AppiumBy.ID, "tv_pay").click()

# 输入密码
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("使用密码")').click()
time.sleep(1)
driver.tap([getSize(525, 1676)])
time.sleep(0.2)
driver.tap([getSize(525, 1676)])
time.sleep(0.2)
driver.tap([getSize(525, 1676)])
time.sleep(0.2)
driver.tap([getSize(886, 1676)])
time.sleep(0.2)
driver.tap([getSize(886, 1676)])
time.sleep(0.2)
driver.tap([getSize(886, 1676)])

# 支付成功

time.sleep(5)
driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView").click()

driver.save_screenshot('pay.png')


# 进入班级
driver.find_element(AppiumBy.ID, "ll_back").click()
driver.find_element(AppiumBy.ID, "goTv").click()
driver.find_element(AppiumBy.ID, "sureIv").click()
time.sleep(1)
driver.save_screenshot('class.png')


input('**** Press to quit..')
driver.quit()