import requests
import logging

def myRequest(url,method,request_data,headers):
    # 1、判断是get还是post请求
    # 2、调用request相应的方法.url,请求数据
    # 3、获取返回值
    # 判断数据是否为空，不为空则转换成字典类型的数据
    #logging.info(headers)
    #logging.info("接口请求地址：%s,方式%s,路径%s" % url%method%request_data)
    if request_data is not None:
        request_data = eval(request_data)

    if method == 'get':
        res = requests.get(url,request_data,headers=headers)
        #res = requests.get(url, method, data2, headers=headers)
    if method == 'post':
        #res = requests.post(url,method,request_data,headers=headers)
        res = requests.post(url, request_data, headers=headers)
        #print("aaaaaaa")
    else:
        res=None
    return res