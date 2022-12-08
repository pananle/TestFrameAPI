# -*- coding: utf-8 -*-

"""
运行用例集：
    python3 run.py
# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'
"""


from Comm.Email import send_email
import pytest
from Comm import Shell
from Conf import config
from Comm import Email
import unittest
import time
import os
import logging
from HTMLTestRunner import HTMLTestRunner



# 获取项目的根目录
test_dir = os.path.join(os.getcwd())

# 自动搜索项目根目录下的所有case，构造测试集；返回TestSuite对象
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

# 实例化TextTestRunner类
# runner = unittest.TextTestRunner(verbosity=2)

now = time.strftime('%Y-%m-%d %H_%M_%S')  # 获取当前日期
result = test_dir + '\\result\\' + now + '_result.html'  # 测试报告的完整路径
log = test_dir + '\\result\\' + now + '_log.txt'  # 日志的完整路径


logging.basicConfig(filename=log, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # filename 日志文件路径 level 日志的级别 format 格式

fp = open(result, 'wb')  # wb方式写入
runner = HTMLTestRunner(stream=fp, title='测试报告', description='cereshop项目接口自动化执行', verbosity=2)  # 构造runner

# 使用run()方法运行测试套件（即运行测试套件中的所有用例）
runner.run(discover)
report_path1 = os.path.join(test_dir, result)
report_path2 = os.path.join(test_dir, log)
report_path = (report_path1,report_path2)
print(report_path)
send_email(report_path)
