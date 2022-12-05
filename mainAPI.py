# -*- coding: utf-8 -*-

"""
运行用例集：
    python3 run.py
# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'
"""
import os
import pytest
from Comm import loggerController
from Comm import Shell
from Conf import config
from Comm import Email
import warnings
warnings.filterwarnings("ignore")


if __name__ == '__main__':
    conf = config.Config()
    log = loggerController.ApiAutoLog()
    log.info('初始化配置文件, path=' + conf.conf_path)

    # 获取报告输出位置
    shell = Shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 定义测试集
    dir = os.path.split(os.path.abspath(__file__))[0]
    test_case_path = dir + '/TestCases/test_init.py'
    args = ['-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)

    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise

    try:
        mail = Email.SendMail()
        mail.sendMail()
    except Exception as e:
        log.error('发送邮件失败，请检查邮件配置')
        raise
