#-*-coding:utf-8-*-
"""
页面基类
所有页面通用的方法封装
dinghanhua
2019-01
"""

from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from datetime import datetime
import os


class BasePage:
    """页面基类"""
    def __init__(self,driver): #构造函数
        self.driver = driver

def openpage(self,url):
        """ 打开页面"""
        self.driver.get(url)
        self.driver.implicitly_wait(10) #隐式等待默认时间
        self.driver.maximize_window() #最大化窗口

def getelement(self,*locator):
        """获取页面元素"""
        return self.driver.find_element(*locator)

def getelements(self,*locator):
        """获取页面元素集"""
        return self.driver.find_elements(*locator)

def getchild(self,pageelement,*locator):
        """获取页面子节点"""
        return pageelement.find_element(*locator)

def getchilds(self,pageelement,*locator):
        """获取元素子节点集"""
        return pageelement.find_elements(*locator)

def getelement_wait_presence(self,*locator):
        ele = WebDriverWait(self.driver, 10, 0.2).until(
            EC.presence_of_element_located(locator)
        )  # 等元素可定位时
        return ele

def refresh(self):
        """刷新页面"""
        self.driver.refresh()

def movetoelement(self,pageelement):
        """鼠标移到pageelement上"""
        actionchains = ActionChains(self.driver)
        actionchains.move_to_element(pageelement).perform()  # 鼠标移到图标上

def wait(self,sec):
        sleep(sec)

def getscreenshot(self,filename="截图"):
        """带有时间戳的截图"""
        screenshot_dir = './screenshot'  # 截图根目录
        if not os.path.exists(screenshot_dir): #不存在则创建该目录
            os.mkdir(screenshot_dir)

        nowdate = datetime.now().strftime('%Y%m%d')  # 当日日期
        screenshot_date_dir = os.path.join(screenshot_dir, str(nowdate))  # 当前日期文件夹
        if not os.path.exists(screenshot_date_dir):
            os.mkdir(screenshot_date_dir)  # 不存在则创建

        nowtime_ms = datetime.now().strftime('%H%M%S%f')  # 时间戳到毫秒级
        filename = nowtime_ms + filename + ".png" # 拼接文件名 时间戳+文件名+.png
        filepath = os.path.join(screenshot_date_dir,filename)
        self.driver.get_screenshot_as_file(filepath) # 截图

def closepage(self):
        """关闭浏览器"""
        self.driver.quit()
