#-*-coding:utf-8-*-
# 订单流程

import time
from selenium import webdriver
import unittest

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.firefox()
        self.driver.get('https://ceresdev.zkthink.com/')
        self.driver.maximize_window()
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def Login(self):
        '''登录pc端'''
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/div[2]/a').click()
        self.driver.find_element_by_css_selector('div.layout div.showTheLogin div.loginCent div.loginForm:nth-child(2) div.loginFormBox div.inputBox:nth-child(1) div.el-input.el-input-group.el-input-group--prepend > input.el-input__inner').send_keys('15738051864')
        self.driver.find_element_by_css_selector('div.layout div.showTheLogin div.loginCent div.loginForm:nth-child(2) div.loginFormBox div.inputBox:nth-child(2) div.el-input.el-input-group.el-input-group--prepend:nth-child(1) > input.el-input__inner').send_keys('9999')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[1]/div/div[2]/button').click()
        time.sleep(2)

    def Search(self):
        # 搜索
        self.driver.find_elements_by_tag_name('input')[0].send_keys('测试')
        self.driver.find_element_by_css_selector('div.layout div.main div:nth-child(1) div.header div.search span.btn.cur-poi > i.icon.el-icon-search').click()
        time.sleep(2)

    def Details(self):
        # 商品详情
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/img').click()
        time.sleep(2)
    def AddCart(self):
        # 购物车
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[2]/div[8]/button[1]').click()
        time.sleep(2)
    def Buy(self):
        # 购买
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[2]/div[8]/button[2]').click()
        time.sleep(2)
    def VxPay(self):
        # 选择支付
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/span').click()
        time.sleep(2)
    def SubmitOrders(self):
        # 提交订单
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/button').click()
        time.sleep(2)
    def CancelPay(self):
        # 取消支付
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[6]/div/div[1]/button').click()
        self.driver.find_element_by_css_selector('body.el-popup-parent--hidden:nth-child(2) div.el-message-box__wrapper:nth-child(6) div.el-message-box div.el-message-box__btns button.el-button.el-button--default.el-button--small.el-button--primary:nth-child(2) > span:nth-child(1)').click()
        self.driver.find_element_by_css_selector('div.layout div.main div.placeOrder.warp div.el-dialog__wrapper:nth-child(9) div.el-dialog div.el-dialog__body div.errorDialog span.dialog-footer button.el-button.btns.el-button--default:nth-child(1) > span:nth-child(1)').click()
        time.sleep(2)

    def CancelOrder(self):
        # 取消订单
        self.driver.find_element_by_css_selector('div.layout div.main div.userCenter.warp div.userCenterInfo div.myOrder div.top div.el-tabs.el-tabs--top:nth-child(1) div.el-tabs__content div.el-tab-pane:nth-child(1) div.sub-main div.orderList div.content:nth-child(1) div.productBox div.product div.right div.operate div.btnContainer > p.btn').click()
        self.driver.find_element_by_css_selector('body.el-popup-parent--hidden:nth-child(2) div.layout div.main div.userCenter.warp div.userCenterInfo div.myOrder div.top div.el-dialog__wrapper.cancelOrder:nth-child(3) div.el-dialog.el-dialog--center div.el-dialog__footer span.dialog-footer button.el-button.rightBtn.el-button--default:nth-child(2) > span:nth-child(1)').click()
        time.sleep(2)

    def ShutDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

