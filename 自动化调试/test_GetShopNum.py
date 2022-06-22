# coding=gbk
import requests
import unittest

class test_GetShopNum(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test01_login(self):
        url = "https://api.kpjushi.cn/auth/login/admin/token/smscode"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        Data = {}

        Data.update(phone='18592034201', smscode="041811")
        r = requests.post(url, headers=headers, data=Data)
        access_token = str(r.json()['data']['access_token'])
        globals()['token'] = access_token
        self.assertTrue(access_token)

    def test02_findOrder(self):
        order_list = []
        url = "https://api.kpjushi.cn/admin/order/adm/order/getListPage?page=1&limit=50&phone="+phone
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'authorization':'Bearer '+globals()['token']
        }

        r = requests.get(url, headers=headers)

        for i in r.json()['data']['records']:
            try:
                orderSn = i['id']
                order_list.append(orderSn)
            except:
                pass
        globals()['order_list'] = order_list
        # print('该用户所有订单号： '+str(globals()['order_list']))

        self.assertTrue(order_list)

    def test03_findShopNum(self):
        shopNum_list = []
        Data = {}
        errOrder_list = []
        headers = {
          'authorization': 'Bearer ' + globals()['token'],
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
          # 'Cookie': 'JSESSIONID='+globals()['JSESSIONID']+'; Path=/; HttpOnly;APP-OAUTH2SESSION='+globals()['APP-OAUTH2SESSION']+'; Path=/; HttpOnly'
}
        url = "https://api.kpjushi.cn/admin/order/adm/order/getOrderDetail"

        for i in globals()['order_list']:
            Data.update(id=i.strip('\r\n\t'))
            r = requests.post(url,headers=headers,data=Data)
            count = 0
            for i in r.json()['data']['orderPayList']:
                if i['payStatus'] == 1:
                    shopNum = i['merchantNo']
                    shopNum_list.append(shopNum)
                else:
                    count += 1
            if count == 0:
                errOrder_list.append(i['orderId'])

        shopNum_listNew = []
        for data in shopNum_list:
            if data not in shopNum_listNew:
                shopNum_listNew.append(data)

        globals()['shopNum_list'] = shopNum_listNew
        globals()['errOrder_list'] = errOrder_list

        print("\n\n")
        print('该账号包含异常商户号为: '+str(globals()['shopNum_list'])+'\n\n')
        print('\n')
        # print('该账号支付失败订单号为: '+str(globals()['errOrder_list']))
        self.assertTrue(shopNum_list)

    def test04_findPayData(self):
        orderInfo = []
        Data = {}
        headers = {
            'authorization': 'Bearer ' + globals()['token'],
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            # 'Cookie': 'JSESSIONID='+globals()['JSESSIONID']+'; Path=/; HttpOnly;APP-OAUTH2SESSION='+globals()['APP-OAUTH2SESSION']+'; Path=/; HttpOnly'
        }
        url = "https://api.kpjushi.cn/admin/order/adm/order/getOrderDetail"

        for i in globals()['order_list']:
            Data.update(id=i.strip('\r\n\t'))
            r = requests.post(url, headers=headers, data=Data)
            print('聚师集团超管平台订单号码: '+str(r.json()['data']['spocOrderNumber']))
            print('\n')
            for i in r.json()['data']['orderPayList']:
                payStatue = ''
                if(i['payStatus']==1):
                    payStatue='创建交易'
                elif(i['payStatus']==2):
                    payStatue='交易成功'
                dict1 = dict(金额 = i['amount'],支付类型=i['payType'],支付方式=i['payWay'],外部订单号=i['id'],商户号=i['merchantNo'],商户名=i['merchantBody'],交易状态=payStatue,创建时间=i['lastUpdateDate'])
                print(dict1)
                print('\n')
                orderInfo.append(dict1)
            print('\n')

    def test05_subId(self):
        if input('******是否申报**********是/否******') == '是':
            print('\n')
            Data = {}
            headers = {
                'authorization': 'Bearer ' + globals()['token'],
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            }
            url = "https://api.kpjushi.cn/admin/order/adm/payRiskRecord/addPayRiskRecordByOrderId"

            for i in globals()['errOrder_list']:
                Data.update(orderId=i.strip('\r\n\t'))
                r = requests.post(url, headers=headers, data=Data)
                print('申报结果： '+r.json()['message'])
            if len(globals()['errOrder_list']) == 0:
                print('当前订单无异常')
        else:
            pass
        print('\n')
        print('\n')
        input('********************点击任意按钮结束********************')


if __name__ == '__main__':
    phone = input('请输入风险提示手机号')
    unittest.main()

