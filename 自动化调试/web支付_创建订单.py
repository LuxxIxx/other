import random,time,os,datetime
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select





class webPay:
  def __init__(self):
    book = xlrd.open_workbook(r'E:/data/webpay_date.xlsx')
    date = book.sheet_by_index(0)
    dateList = date.row_values(1)
    # 赋值
    self.className = str(dateList[0]).strip('\r\n\t')
    self.loginNum = str(dateList[1]).strip('\r\n\t')
    self.name = str(dateList[2]).strip('\r\n\t')
    self.addr = str(dateList[3]).strip('\r\n\t')
    if len(self.loginNum) == 0:
      self.loginNum = 0
    else:
      self.loginNum = int(dateList[1])
    if str(dateList[4]).strip('\r\n\t') == '是':
      self.isPay = True
    else:
      self.isPay = False

  def GetPhoneNum(self):
    seed = "1234567890"
    sa = []
    for i in range(9):
      sa.append(random.choice(seed))
    phoneNum = '13' + ''.join(sa)
    return  phoneNum




if __name__ == '__main__':
    Data=webPay()
    wd = webdriver.Chrome(service=Service(r'd:\driver\chromedriver.exe'))
    wd.implicitly_wait(20)

    wd.get('https://www.jushispoc.com/#/home')
    wd.maximize_window()
    time.sleep(2)


    # 登录
    wd.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div/div[2]/div[2]/div/div/div[2]').click()

    # 构建登录账号
    if Data.loginNum == 0:
      loginNum = Data.GetPhoneNum()
      wd.find_element(By.CSS_SELECTOR, "input[placeholder='请输入手机号']").send_keys(loginNum)
      Data.loginNum = loginNum
    else:
      wd.find_element(By.CSS_SELECTOR, "input[placeholder='请输入手机号']").send_keys(Data.loginNum)

    wd.find_element(By.CSS_SELECTOR,"input[placeholder='请输入验证码']").send_keys('911106')
    wd.find_element(By.CSS_SELECTOR,"button[class='el-button el-button--default login']").click()
    time.sleep(1)

    # 验证登录
    if wd.find_element(By.CSS_SELECTOR,"button[class='el-button tx el-button--primary el-dropdown-selfdefine']"):
      print("pass")
    else:
      print('fail')
    # wd.find_element(By.CSS_SELECTOR,"")
    # wd.find_element(By.XPATH,'')

    # 进入班级购买页
    time.sleep(1)
    wd.find_elements(By.CSS_SELECTOR,"div[class='nav_item']")[0].click()
    time.sleep(1)
    wd.find_element(By.CSS_SELECTOR,'input[placeholder="输入关键词搜索课程"]').send_keys(Data.className)
    wd.find_element(By.CSS_SELECTOR,'button[class ="el-button el-button--default"]').click()
    time.sleep(1)
    wd.find_element(By.XPATH, '// *[ @ id = "app"] / div[2] / div[3] / div / div').click()
    # wd.find_element(By.XPATH,'//h1[contains(text(),"'+Date.className+'")]').click()
    time.sleep(1)
    wd.find_element(By.XPATH,'//span[contains(text(),"立刻报名")]').click()


    # 收货人信息
    wd.find_element(By.XPATH,'//span[contains(text(),"添加收货信息")]').click()
    time.sleep(0.5)
    wd.find_element(By.CSS_SELECTOR,'input[placeholder="请填写收货人姓名"]').send_keys(Data.name)
    select1 = Select(wd.find_elements(By.CSS_SELECTOR,"div[class='distpicker-address-wrapper']>select")[0])
    select1.select_by_visible_text('北京市')
    time.sleep(0.5)
    select2 = Select(wd.find_elements(By.CSS_SELECTOR,"div[class='distpicker-address-wrapper']>select")[1])
    select2.select_by_visible_text('北京市')
    time.sleep(0.5)
    select3 = Select(wd.find_elements(By.CSS_SELECTOR,"div[class='distpicker-address-wrapper']>select")[2])
    select3.select_by_visible_text('丰台区')
    time.sleep(0.5)
    wd.find_element(By.CSS_SELECTOR,'input[placeholder="请填写详细地址"]').send_keys(Data.addr)
    wd.find_element(By.CSS_SELECTOR,'input[placeholder="请填写收货人电话"]').send_keys(Data.loginNum)
    wd.find_element(By.CSS_SELECTOR,"div[class='save_btu']").click()
    time.sleep(1)
    wd.find_element(By.CSS_SELECTOR,"div[class='placeorder_submit']").click()
    time.sleep(6)
    wd.find_element(By.XPATH,'//span[contains(text(),"同意本条款,继续支付")]').click()
    time.sleep(0.5)
    wd.find_element(By.CSS_SELECTOR,"div[class='placeorder_submit']").click()
    time.sleep(5)
    wd.save_screenshot(r"E:\\printscreen\pay.png")

    time.sleep(2)

    os.system('python web支付_手机支付.py')




