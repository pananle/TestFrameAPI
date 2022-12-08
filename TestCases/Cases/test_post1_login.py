# -*- coding:utf-8 -*-
# 登录用例
import logging
import requests
import unittest
import demjson

from urllib import parse
from TestCases.lib import login
from ruamel import yaml


class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.url = "https://ceres.zkthink.com/api/app/login"

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_00(self):  # 代码逻辑::设置正确账号密码，发送post请求
        '''登录成功'''
        headers = {"Content-Type": "application/json"}
        data = login.postLoginData()
        r = requests.post(self.url,data=demjson.encode(data),headers=headers)
        yamlpath = r'D:\TestFrameAPI\TestCases\lib\token.yaml'  # 保存文件路径
        # 提取token字段
        tokenValue = {
            'token': r.json()["data"]["token"]
        }
        with open(yamlpath, "w", encoding="utf-8") as f:
            yaml.dump(tokenValue, f, Dumper=yaml.RoundTripDumper)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(f"case:授权登录成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_01(self):
        '''验证码错误'''
        headers = {"Content-Type": "application/json"}
        data = login.postLoginData()
        data['verificationCode'] = '1234'
        r = requests.post(self.url, data=demjson.encode(data), headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "验证码有误"
        logging.info(f"case:验证码错误\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_02(self):
        '''用户未注册'''
        headers = {"Content-Type": "application/json"}
        data = login.postLoginData()
        data['phone'] = '15738099999'
        r = requests.post(self.url, data=demjson.encode(data), headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "用户未注册"
        logging.info(f"case:用户未注册\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

if __name__ == '__main__':
    unittest.main()
