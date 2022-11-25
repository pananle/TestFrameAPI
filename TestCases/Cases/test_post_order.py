# -*- coding:utf-8 -*-
# 登录用例

import requests
import unittest
import logging
import demjson
from urllib import parse
from TestCases.lib import order
from TestCases.lib.re_token import get_token

class Test_order(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.token = get_token()
        # print("获取到当前用例token值：%s" % self.token)
        self.url = "https://ceres.zkthink.com/api/order/submit" #提交订单
        self.url1 = "https://ceres.zkthink.com/api/order/cancel" #取消订单

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_00(self):  # 代码逻辑::
        '''提交订单'''
        headers = {"Content-Type": "application/json","Authorization":self.token}
        data = order.postOrderData()
        data['skuId'] = '2091'
        r = requests.post(self.url,data=demjson.encode(data),headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(
            f"case:授权登录，成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_01(self):
        '''取消订单'''
        headers = {"Content-Type": "application/json","Authorization":self.token}
        data = order.postOrderData()
        data['orderId'] = '2'
        r = requests.post(self.url, data=demjson.encode(data), headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(
            f"case:授权登录，成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_02(self):
        '''再次购买'''
        headers = {"Content-Type": "application/json","Authorization":self.token}
        data = order.postOrderData()
        data['number'] = '1'
        r = requests.post(self.url, data=demjson.encode(data), headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(
            f"case:授权登录，成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_03(self):
        '''删除订单'''
        headers = {"Content-Type": "application/json","Authorization":self.token}
        data = order.postOrderData()
        data['skuId'] = '2091'
        r = requests.post(self.url, data=demjson.encode(data), headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(
            f"case:授权登录，成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
