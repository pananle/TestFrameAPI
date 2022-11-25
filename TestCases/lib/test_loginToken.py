#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 外部接口可以获取token，内部接口不可以获取token
import requests
from ruamel import yaml
import json


def test_loginToken():
    '''token截取'''
    host = 'https://ceres.zkthink.com/api/app/'  # 接口地址ip与port
    url = host + "login"
    # 登录的参数数据
    data = {
        "phone": "15738051864",
        "verificationCode": "9999",
        "type": "2",
        "terminal": 5
    }
    # 登录请求头部信息
    headers = {'Content-Type': 'application/json'}
    # 初始化url请求对象
    response = requests.post(url=url, data=json.dumps(data), headers=headers)

    print(response.text)
    print(response.status_code)
    print(response.json()["data"]["token"])
    # return response.json()["token"]

    # 把token值写入配置文件中
    yamlpath = r'D:\TestFrame\TestCases\lib\token.yaml'  # 保存文件路径
    # 提取token字段
    tokenValue = {
        'token': response.json()["data"]["token"]
    }
    with open(yamlpath, "w", encoding="utf-8") as f:
        yaml.dump(tokenValue, f, Dumper=yaml.RoundTripDumper)


if __name__ == "__main__":
    test_loginToken()
