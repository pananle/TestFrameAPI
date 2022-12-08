# -*- coding:utf-8 -*-
# 搜索用例
import requests
import unittest
from urllib import parse
from TestCases.lib import search
import logging
class Test_Search(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # 商品
        self.url = "https://ceres.zkthink.com/api/app/getSearchProducts"
        # 店铺
        self.url2 = "https://ceres.zkthink.com/api/shop/getShops"

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_00(self):  # 代码逻辑::
        '''商品搜索成功'''
        headers = {"Content-Type": "application/json"}
        data = search.getSearchData()
        r = requests.get(self.url,params=data,headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(f"case:商品搜索成功\n请求地址：{r.request.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.urlparse(r.url)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


    def test_01(self):  # 代码逻辑::
        '''店铺搜索成功'''
        headers = {"Content-Type": "application/json"}
        data = search.getSearchData()
        r = requests.get(self.url2,params=data,headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(f"case:店铺搜索成功\n请求地址：{r.request.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.urlparse(r.url)}\n响应头：{r.headers}\n响应正文：{r.text}\n")

    def test_02(self):  # 代码逻辑::
        '''搜索输入为空'''
        headers = {"Content-Type": "application/json"}
        data = search.getSearchData()
        data["search"] = ''
        r = requests.get(self.url, params=data, headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(f"case:搜索输入为空\n请求地址：{r.request.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.urlparse(r.url)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


    def test_03(self):  # 代码逻辑::
        '''搜索输入为不存在的'''
        headers = {"Content-Type": "application/json"}
        data = search.getSearchData()
        data["search"] = '不存在的'
        r = requests.get(self.url, params=data, headers=headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["message"] == "成功"
        logging.info(f"case:搜索不存在的关键字\n请求地址：{r.request.url}\t请求方式:{r.request.method}\n请求头：{r.request.headers}\n请求正文：{parse.urlparse(r.url)}\n响应头：{r.headers}\n响应正文：{r.text}\n")


if __name__ == '__main__':
    unittest.main()

