import requests
import re
import json

class Login:
    #获取token的函数
    def get_token(self,url,data):
        res = requests.post(url, data)
        #print(res.text)
        print(res.content)
        print(res.status_code)
        return res.json()["data"]["token"],res.cookies.get("SESSION") #返回token的值

if __name__ =='__main__':
    url="http://47.99.40.208:9010/app/user/loginTest"
    data=""
    login = Login()
    token, SESSION = login.get_token(url, data)
    header = {"token": token, "cookie": "SESSION=" + SESSION}
    url2="http://47.99.40.208:9010/app/order/createOrderApp"
    data2={"isSure": "true","goodsCode": "651cdf2d1a284761b2c99ecb88dc18e7","goodsHistoryCode": "929120d2bf6e4bb698c3dbc3500530d7","goodsSkuRelCode": "hoursRent","gameCode":"973594c8026f48f68fe10f8ce9a1cdc8","buyType":"2","beginTime":"2018-10-31 23:00:00","finishTime":"2018-11-01 00:00:00","totalAmount":"0.02","goodsAmount":"0.01","pledgeAmount":"0.01","groupName":"时租","show":"false","countTime":"3","description":"温馨提示：交易猫工作人员不会以任何理由在游戏里向所要任何游戏账号、交易猫账号、游戏物品等。请提防诈骗信息，祝您游戏愉快！"}
    data3={"isSure": "true","goodsCode": "651cdf2d1a284761b2c99ecb88dc18e7","goodsHistoryCode": "929120d2bf6e4bb698c3dbc3500530d7","goodsSkuRelCode": "hoursRent","gameCode":"973594c8026f48f68fe10f8ce9a1cdc8","buyType":"2","beginTime":"2018-10-30 23:00:00","finishTime":"2018-10-31 00:00:00","totalAmount":"0.02","goodsAmount":"0.01","pledgeAmount":"0.01","groupName":"时租","show":"false","countTime":"3","description":"温馨提示：交易猫工作人员不会以任何理由在游戏里向所要任何游戏账号、交易猫账号、游戏物品等。请提防诈骗信息，祝您游戏愉快！"}

    print(header)
    res=requests.post(url2,data3,headers=header)
    print(res.text)


