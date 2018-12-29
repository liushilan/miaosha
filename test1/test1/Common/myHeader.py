import requests#python的http库
import logging

def Get_token_session():
    url = "http://47.99.40.208:9010/app/user/loginTest"
    data = ""
    res = requests.post(url, data)
    token, SESSION=res.json()["data"]["token"], res.cookies.get("SESSION")
    header = {"token": token, "cookie": "SESSION=" + SESSION}
    logging.info(header)
    return  header # 返回header的值
