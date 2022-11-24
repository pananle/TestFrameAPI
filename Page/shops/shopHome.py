# coding:utf-8
# 页面对象
"""
首页
LOCATOR : 所有页面元素的定位器
首页页面元素的定位和操作均写在该类中
"""
from Page import basePage
from selenium.webdriver.common.by import By
import logging;logging.basicConfig(level=logging.INFO)

class IndexPage(basePage.BasePage):
    """
    首页类
    """
    # LOCATOR
    _stylelist_LOCATOR = (By.CSS_SELECTOR, "#styleList li[data-style]")
    _current_LOCATOR = (By.CSS_SELECTOR, "#styleList .current")
    _latestInfoList_LOCATOR = (By.CSS_SELECTOR, "ul#latestInfoList>li")
    _mystyle_name__LOCATOR = (By.ID, "myStyle_name_")
    _mystyle_name_LOCATOR = (By.ID, "myStyle_name")
    _style_desc_LCOATOR = (By.CLASS_NAME, "style-desc")
    _myStyle_remark_LOCATOR = (By.ID, "myStyle_remark")
    _read_strategy_LOCATOR = (By.CLASS_NAME, "read-strategy")
    _style_desc_item_LOCATOR = (By.CLASS_NAME, "style-desc-item")
    _profit_percent_LOCATOR = (By.CLASS_NAME, "profit-percent")
    _style_name_LOCATOR = (By.CLASS_NAME, "style-name")
    _style_description_LOCATOR = (By.CLASS_NAME, "style-description")

    def open_index_page(self, sso):
        """打开首页"""

        domain = 'https://ceres.zkthink.com'
        indexurl = '/pc/#/index'
        url = domain + indexurl
        self.openpage(url)
        self.getscreenshot("Indexpage打开页面")

    def get_styleList(self):
        """获取策略风格列表"""
        styleList = self.getelements(*IndexPage._stylelist_LOCATOR)  # 策略列表
        return styleList

    def get_current_style(self):
        """获取当前策略信息"""
        current = self.getelement(*IndexPage._current_LOCATOR)  # 当前策略
        self.current_style = current.get_attribute("data-style")  # 当前策略类型
        self.current_name = current.text  # 当前策略名称

    def choose_style(self, styleindex):
        """选择index = styleindex的策略风格"""
        stylelist = self.get_styleList()  # 获取策略列表
        try:
            style = stylelist[styleindex]
            self.select_style = style.get_attribute("data-style")  # 选择的策略类型
            self.select_name = style.text  # 选择的策略名称
            style.click()  # 点击策略
            self.wait(1)
            self.getscreenshot("Indexpage策略信息")
            self.get_current_style()  # 选择之后获取策略信息
        except Exception as msg:
            print(msg)

    def check_SelectEqCurrent(self):
        """验证选择的风格与显示的风格是否一致"""
        if self.select_name == self.current_name and self.select_style == self.current_style:
            return True

    def get_level_info_list(self):
        """获取右侧显示的策略信息列表"""
        level_desc_items = self.getelements(*IndexPage._style_desc_item_LOCATOR)  # 取所有的策略详情
        level_info_list = [item for item in level_desc_items if item.is_displayed()]  # 取页面显示的策略详情
        return level_info_list

    def get_level_info(self, levelindex):
        """获取策略信息"""
        levellist = self.get_level_info_list()
        try:
            level = levellist[levelindex]  # 获取策略信息
            percentM3 = self.getchild(level, *IndexPage._profit_percent_LOCATOR)
            name = self.getchild(level, *IndexPage._style_name_LOCATOR)
            description = self.getchild(level, *IndexPage._style_description_LOCATOR)
            read_strategy = self.getchild(level, *IndexPage._read_strategy_LOCATOR)

            self.percentM3 = float(percentM3.text[:-1])  # 获取3个月收益
            self.name = name.text  # 策略名称
            self.description = description.text  # 策略描述
            self.read_strategy = read_strategy
            self.data_code = self.read_strategy.get_attribute("data-code")  # 策略代码
        except Exception as msg:
            print(msg)

    def get_mystyle(self):
        """获取我的风格"""
        self.wait(0.5)
        myStyle_nameele = self.getelement(*IndexPage._mystyle_name_LOCATOR)
        self.myStyle_name = myStyle_nameele.text[1:-1]  # 我的风格

        style_desc = self.getelement(*IndexPage._style_desc_LCOATOR)
        self.movetoelement(style_desc)  # 移动鼠标至问号图标
        myStyle_intips = self.getelement_wait_presence(*IndexPage._mystyle_name__LOCATOR)  # 等元素显示时识别
        self.getscreenshot("Indexpage气泡")
        self.myStylename_intips = myStyle_intips.text[:-1]
        self.mystyle_remark = self.getelement(*IndexPage._myStyle_remark_LOCATOR).text  # tip里的风格说明

    def check_mystyle(self):
        """验证风险等级页面和tip是否一致"""
        self.get_mystyle()
        logging.info("用户类型：{0}，tips里的用户类型：{1}".format(self.myStyle_name, self.myStylename_intips))
        if self.myStyle_name == self.myStylename_intips and self.myStyle_name in self.mystyle_remark:
            return True

    def check_default_ismystyle(self):
        """验证默认策略与用户风险等级匹配"""
        self.refresh()  # 刷新，自动更新到用户匹配的等级
        self.wait(1)
        self.get_current_style()
        self.get_mystyle()
        logging.info("当前策略：{0}，用户风格：{1}".format(self.current_name, self.myStyle_name))
        if self.current_name == self.myStyle_name:
            return True

    def clicklink_read_strategy(self, levelindex=0):
        """点击查看策略"""
        self.get_level_info(levelindex)  # 选页面显示的第levelindex个策略
        self.read_strategy.click()  # 点击查看策略
        self.wait(1)
        self.getscreenshot("Indexpage点击查看策略跳转到策略")
        return self.driver, self.data_code  # 跳转到了策略页面

