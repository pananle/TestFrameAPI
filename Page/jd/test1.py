# coding:utf-8
"""
首页相关用例
"""

from APIs import base_api
from Page.shops.shopHome import IndexPage
from Page.jd.StrategyPage import StrategyPage
from Comm.launch_browser import launch_browser
import unittest
from ddt import ddt,data

@ddt
class IndexPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        sso = "https://ceres.zkthink.com/pc/#/index"
        driver = launch_browser('firefox') # 启动浏览器
        cls.page = IndexPage(driver) # 实例化首页页面对象
        cls.page.open_index_page(sso) # 打开首页
        cls.fund = base_api() # 接口对象


    @classmethod
    def tearDownClass(cls):
        cls.page.closepage()

    def test01_check_mystyle(self):
        """验证首页风险等级与tips里的一致"""
        result = self.page.check_mystyle()
        self.assertTrue(result,"页面风险等级与tips里的不一致")

    def test02_default_style(self):
        """验证页面默认策略与用户风险等级一致"""
        result = self.page.check_default_ismystyle()
        self.assertTrue(result,"页面默认策略与用户风险等级不一致")

    def test03_default_data(self):
        """验证默认策略的数据正确性"""
        self.check_levels_data()

    @data(*range(5))
    def test04_choose_style(self,styleindex):
        """验证各策略风格的数据正确性"""
        with self.subTest('choose_style_%s'%styleindex): #创建测试子项，一次循环fail会继续执行下一次循环
            self.page.choose_style(styleindex) #选择style
            self.assertTrue(self.page.check_SelectEqCurrent(),"所选风格与显示的风格不一致")
            self.check_levels_data()

    def test05_click_btn(self):
        """验证点击查看策略按钮，跳转页面风格与所点击风格一致"""
        driver,data_code_index = self.page.clicklink_read_strategy() # 返回的是策略页面和code
        newpage= StrategyPage(driver) # 点击之后成了策略页面对象
        newpage.get_strategyinfo()#  验证策略页面的类型与点击的一致
        self.assertEqual(data_code_index,newpage.strategycode,"点击的策略与跳转后的策略code不一致")

    def check_levels_data(self):
        """比较各level数据与接口数据是否一致"""
        for levelindex in range(3):  # 验证右侧三个level数据正确性
            with self.subTest(('check_level_data:level%s') % (levelindex + 1)):
                self.page.get_level_info(levelindex)  # 循环获取右侧的信息

                self.fund.get_fund_strategy(self.page.data_code, latest=-1)  # 获取接口策略信息
                self.fund.get_fund_percentM3(self.page.data_code)  # 获取3个月收益率

                actual_result = [self.page.data_code, self.page.percentM3, self.page.name,
                                 self.page.description]  # 实际结果
                expect_result = [self.fund.code, self.fund.percentM3, self.fund.name, self.fund.summary]  # 预期结果
                self.assertEqual(actual_result, expect_result, "首页数据和接口数据不一致")


if __name__ == '__main__':
    unittest.main()