# coding:utf-8
"""
启动浏览器
"""

from selenium import webdriver


def launch_browser(browsername):
    if browsername.lower() == "chrome":
        driver = webdriver.Chrome()

    elif browsername.lower() == "firefox":
        driver = webdriver.Firefox()

    elif browsername.lower() == 'ie':
        driver = webdriver.Ie()

    else:
        raise Exception("sorry,该浏览器不在启动范围内，请安装驱动并修改launch_browser函数")

    return driver