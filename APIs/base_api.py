import logging
import random
import importlib
import copy
import json
import unittest
from hashlib import md5
from ipaddress import ip_address
from Comm.compare import CompareStr

logger = logging.getLogger('main.api')
req_prefix = 'req.'
res_prefix = 'res.'


def _separate_data(data, prefix='req.'):
    pfx = prefix
    result = {}
    for key, value in data.items():
        if key.startswith(pfx):
            req_key = key[len(pfx):]
            result[req_key] = value
    return result


def _get_cmd(key, dict_name='payload'):
    separator = '.'
    cmd = dict_name
    if separator in key:
        data_key = key.split(separator)
        for each in data_key:
            if each.isdigit():
                cmd = cmd + '[' + each + ']'
            else:
                cmd = cmd + '[\'' + each + '\']'
        cmd = cmd + ' = value'
    else:
        cmd = cmd + '[key] = value'
    return cmd


def check_result(unittest_testcase, x, y):
    # 只有x,y完全相同才能通过，任意不同则返回失败。建议自己在用例中做结果检查
    testcase = unittest_testcase
    diff = CompareStr(x, y)
    testcase.assertEqual(x, y)


class BaseAPI(object):
    def __init__(self, api):
        self.api = api
        self.api_name = None
        self.url = ''
        self.req_template = {}
        self.res_template = {}
        self._get_api_param()

    def _get_api_param(self):
        """动态加载API定义文件，获取文件中定义的API参数"""
        try:
            m = importlib.import_module(self.api)
            self.api_name = m.API_NAME
            self.url = m.url
            self.req_template = m.req_param
            self.res_template = m.res_param
        except Exception as e:
            logger.error('error info : %s' % e)

    def payload(self, data=None):
        payload = copy.deepcopy(self.req_template)
        if data:
            req_pre = '.'.join([self.api_name, req_prefix])
            req_data = _separate_data(data, req_pre)
            for key, value in req_data.items():
                cmd = _get_cmd(key, 'payload')
                exec(cmd)
        return payload

    def load_expected(self, data=None):
        expected = copy.deepcopy(self.res_template)
        if data:
            res_pre = '.'.join([self.api_name, res_prefix])
            res_data = _separate_data(data, res_pre)
            for key, value in res_data.items():
                cmd = _get_cmd(key, 'expected')
                exec(cmd)
        return expected

