# -*- coding:utf-8 -*-
# 登录用例

import requests
import unittest
import logging
import demjson
from urllib import parse
from TestCases.lib import cart
from TestCases.lib.re_token import get_token

class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.token = get_token()
        print("获取到当前用例token值：%s" % self.token)
        self.url = "https://ceres.zkthink.com/api/cart/addCart" #添加购物车
        self.url1 = "https://ceres.zkthink.com/api/cart/delete" #删除购物车商品
        self.url2 = "https://ceres.zkthink.com/api/cart/updateNumber" #修改购物车数量

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_00(self):  # 代码逻辑::
        '''添加购物车成功'''
        headers = {"Content-Type": "application/json","Authorization":self.token}
        data = cart.postCatData()
        data['skuId'] = '2091'
        r = requests.post(self.url,data=demjson.encode(data),headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(
            f"case:授权登录，成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_01(self):
        '''购物车商品加数量'''
        headers = {"Content-Type": "application/json","Authorization":self.token}
        data = cart.postCatData()
        data['number'] = '2'
        r = requests.post(self.url2, data=demjson.encode(data), headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(
            f"case:授权登录，成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_02(self):
        '''购物车商品减数量'''
        headers = {"Content-Type": "application/json","Authorization":self.token}
        data = cart.postCatData()
        data['number'] = '1'
        r = requests.post(self.url2, data=demjson.encode(data), headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(
            f"case:授权登录，成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_03(self):
        '''移除购物车'''
        headers = {"Content-Type": "application/json","Authorization":self.token}
        data = cart.postCatData()
        data['skuId'] = '2091'
        r = requests.post(self.url1, data=demjson.encode(data), headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(
            f"case:授权登录，成功\n请求地址：{r.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.unquote(r.request.body)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()
