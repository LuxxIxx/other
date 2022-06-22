import datetime,xlrd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


class CreatOrder:
  def __init__(self,num):
    book = xlrd.open_workbook(r'E:/data/creatorder.xlsx')
    date = book.sheet_by_index(0)
    dateList = date.row_values(num)
    self.count = date.nrows
    # 赋值
    self.url = str(dateList[0]).strip('\r\n\t')
    self.shop = str(dateList[1]).strip('\r\n\t')
    self.phone = str(dateList[2]).strip('\r\n\t')
    self.name = str(dateList[3]).strip('\r\n\t')
    self.addr = str(dateList[4]).strip('\r\n\t')
    self.product = str(dateList[5]).strip('\r\n\t')
    self.orderNum = 0
    if len(self.url) == 0:
      self.url = 'https://t1-jspc.gzjushiwang.com/#/clazzCourseDetail/1507173532602933249/1507173455721340929/1'
    if len(self.phone) == 0:
      self.phone = 13000000001
    else:
      self.phone = int(dateList[2])
    if len(self.name) == 0:
      self.name = '测试人员'
    if len(self.addr) == 0:
      self.addr = '测试地址'

    if str(dateList[6]).strip('\r\n\t') == '是':
      self.isPay = True
    else:
      self.isPay = False


if __name__ == '__main__':
    # <editor-fold desc="进入测试平台">
    book = xlrd.open_workbook(r'E:/data/creatorder.xlsx')
    date = book.sheet_by_index(0)

    wd = webdriver.Chrome(service=Service(r'd:\driver\chromedriver.exe'))
    wd.implicitly_wait(20)

    wd.get('https://t1-jsui.gzjushiwang.com/')
    wd.maximize_window()

    wd.find_elements(By.CLASS_NAME, 'ivu-input-default')[0].send_keys('17812322339')
    wd.find_elements(By.CLASS_NAME, 'ivu-input-default')[1].send_keys('123456')
    wd.find_element(By.CLASS_NAME, 'ivu-btn-long').click()
    wd.find_element(By.CSS_SELECTOR, 'div[title="' + date.row_values(1)[1] + '"][class="chooseInner_name"]').click()
    # </editor-fold>


    for num in range(date.nrows-1):
        co = CreatOrder(num+1)

        # <editor-fold desc="编辑订单">
        wd.find_element(By.XPATH,'//div[@class="ivu-menu-submenu-title"]/span[contains(text(),"订单管理")]').click()
        wd.find_element(By.XPATH,"//li[@class='ivu-menu-item']/span[contains(text(),'添加对公支付订单')]").click()
        wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[2]/div/div/input').send_keys(co.url)
        wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[7]/div/div[1]/input').send_keys(co.phone)
        wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[9]/div/div[1]/input').send_keys(co.name)
        wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[10]/div/div/input').send_keys(co.phone)
        time.sleep(0.5)
        wd.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[11]/div/div').click()
        wd.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[11]/div/div/div[2]/ul[2]/li[1]').click()
        time.sleep(0.5)
        wd.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[12]/div/div').click()
        wd.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[12]/div/div/div[2]/ul[2]').click()
        time.sleep(0.5)
        wd.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[13]/div/div/div[1]').click()
        wd.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[13]/div/div/div[2]/ul[2]/li[4]').click()
        wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[14]/div/div/input').send_keys(co.addr)
        wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/form/div[16]/div/button').click()
        # </editor-fold>

        # <editor-fold desc="线下支付配置">
        time.sleep(1)
        wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/span').click()
        wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/ul[2]/li[2]').click()
        wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div/form/div[3]/div/div/div/div[1]/input').send_keys(co.name)
        wd.find_element(By.CSS_SELECTOR,"input[type='file'][accept='.jpg,.png,.jpeg']").send_keys(r'E:\\自动化调试\image\test.jpg')
        time.sleep(4)
        # </editor-fold>

        # <editor-fold desc="提交订单">
        wd.find_elements(By.CSS_SELECTOR,"div[style='margin-left: 100px;']>button[type='button']")[1].click()
        time.sleep(1)
        # </editor-fold>

        # <editor-fold desc="检查是否提交成功">
        if wd.find_element(By.XPATH,'/html/body/div[43]/div[2]/div/div'):
            print('pass')
            time.sleep(1)
            wd.find_element(By.XPATH,'/html/body/div[43]/div[2]/div/div/div/div/div[3]/button').click()
        else:
            print('fail')
        # </editor-fold>

        if co.isPay == True:
            # <editor-fold desc="进入订单审核，根据电话搜索到我的订单">
            wd.refresh()
            time.sleep(3)
            wd.find_element(By.XPATH,'//div[@class="ivu-menu-submenu-title"]/span[contains(text(),"订单管理")]').click()
            wd.find_element(By.XPATH,"//li[@class='ivu-menu-item']/span[contains(text(),'对公转账订单')]").click()
            wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[9]/div/div/input').send_keys(co.phone)
            wd.find_element((By.XPATH),'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[17]/div/button[1]').click()
            # </editor-fold>

            # <editor-fold desc="检查首位订单状态，是否为刚刚提交的订单">
            list = wd.find_elements(By.CSS_SELECTOR,'table[style="width: 5209px;"]>tbody[class="ivu-table-tbody"]')
            if len(list)!=0:
                productName = wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/span').text
                ischeck = wd.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[36]/div/div/div/span').text
                if productName==co.product and ischeck=="审核中":
                    print("pass")
                    co.orderNum = wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[10]/div/span').text
                else:
                    print(ischeck)
                    print(productName)
            else:
                print('fail;')
            # </editor-fold>

            # <editor-fold desc="进入订单审核界面">
            wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[9]/div/div/input').clear()
            wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[1]/div/div/input').send_keys(co.orderNum)
            wd.find_element((By.XPATH),'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[17]/div/button[1]').click()
            time.sleep(1)
            move = wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div')
            ActionChains(wd).move_to_element(move).perform()
            time.sleep(0.5)
            wd.find_elements(By.CSS_SELECTOR,"div[class='ivu-select-dropdown ivu-dropdown-transfer']>ul>li")[6].click()
            # </editor-fold>

            # <editor-fold desc="提交审核">
            time.sleep(1)
            wd.find_element(By.XPATH,'//label[contains(text(),"通过")]').click()
            dateTime = datetime.date.today()
            wd.find_elements(By.CSS_SELECTOR,"input[class='ivu-input ivu-input-default ivu-input-with-suffix']")[2].send_keys(str(dateTime)+' 00:00:00')
            time.sleep(2)
            enter = wd.find_elements(By.CSS_SELECTOR,'div[class="ivu-modal-content ivu-modal-content-drag"]>div[class="ivu-modal-footer"]>button[class="ivu-btn ivu-btn-primary"]>span')
            if len(enter) == 10:
                enter[8].click()
            else:
                enter[6].click()
            # </editor-fold>

            # <editor-fold desc="通过订单号搜索订单，检查是否审核通过">
            time.sleep(1)
            wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[1]/div/div/input').clear()
            wd.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[1]/div/div/input').send_keys(co.orderNum)
            wd.find_element((By.XPATH),'//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/form/div[17]/div/button[1]').click()
            time.sleep(2)
            ischeck = wd.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[36]/div/div/div/span').text
            if ischeck == '审核通过':
                print("pass")
            else:
                print('fail')
            # </editor-fold>

    wd.quit()