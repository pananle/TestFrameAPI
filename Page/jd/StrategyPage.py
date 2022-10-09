#coding:utf-8

"""
策略页面类
LOCATOR : 所有页面元素的定位器
策略页面元素的定位和操作均写在该类中
"""

from Page import basePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import logging;logging.basicConfig(level=logging.INFO)


class StrategyPage(basePage.BasePage):
    """
   策略页面类
    """

    #LOCATOR
    _selectedStrategyName_locator = (By.ID, "selectedStrategyName")
    _selectedstragegy_locator  = (By.CSS_SELECTOR, "#strategyList dd.actived")
    _navinfo_locator = (By.CSS_SELECTOR,"#estimationRightInfo .ifund-zf li")
    _groupRiseTbody_locator = (By.ID, "groupRiseTbody")
    _h1_locator = (By.TAG_NAME,"h1")
    _p_locator = (By.TAG_NAME,"p")
    _span_loacator = (By.TAG_NAME,"span")
    _tr_locator = (By.TAG_NAME,"tr")
    _td_locator = (By.CSS_SELECTOR,"td div")
    _dd_locator = (By.TAG_NAME,"dd")
    _pattern_locator = (By.CSS_SELECTOR,"#groupTechContainer .switch-header-i.actived")
    _patterns_locator = (By.CSS_SELECTOR,"#groupTechContainer .switch-header-i")
    _peroid_locator = (By.CSS_SELECTOR,"#groupTechContainer .switch-container li.actived")
    _name_locator = (By.ID,"selectedStrategyName")
    _strategystyle_locator = (By.CSS_SELECTOR, "#poptype li")
    _strategylevel_locator = (By.CSS_SELECTOR, "#strategyList dd")
    _peroids_locator = (By.CSS_SELECTOR,"#groupTechContainer .switch-container .charttype li")
    _startdate_locator = (By.ID,"mdStart")
    _spchart_locator = (By.ID, "spchartType")
    _percentRun_locator = (By.ID, "percentRun")
    _percentDiff_locator = (By.ID, "percentDiff")
    _yield_locator = (By.ID,"yield")
    _mdStartEnd_locator = (By.ID, "mdStart-End")
    _adjustdate_locator = (By.ID,"selAdjustDates")
    _strategyinfo_locator = (By.ID, "strategyinfo")
    _memo_locator = (By.CLASS_NAME, "s-tips")
    _details_locator = (By.CSS_SELECTOR, ".s-details dl")
    _maxretrace_locator = (By.ID, "maxretrace")
    _sharpeRun_locator = (By.ID, "sharpeRun")
    _sharpeDiff_locator = (By.ID, "sharpeDiff")
    _xpRate_locator = (By.ID, "xpRate")
    _js_totop = "scrollTo(0,0)"
    _js_trends = 'document.getElementsByClassName("ifund-module-i")[1].scrollIntoView()'
    _js_adjustdate = 'document.getElementById("selAdjustDates").scrollIntoView()'
    _js_percents = 'document.getElementById("groupRiseTbody").scrollIntoView()'



    def open_strategy_page(self,sso):
        """ 打开策略页面 """
        domain = "http://testdomain"
        strategyurl = '/strategy'
        url = domain + strategyurl + '?' + sso
        self.openpage(url)

    def get_code(self):
        self.strategycode = self.getelement(*StrategyPage._selectedstragegy_locator).get_attribute("data-code") #获取策略code
        return self.strategycode

    def get_strategyinfo(self):
        """获取页面策略代码、名称信息"""
        self.selectedStrategyName = self.getelement(*StrategyPage._selectedStrategyName_locator).text  # 选中的策略风格名称
        self.selectedstragegy = self.getelement(*StrategyPage._selectedstragegy_locator)

        self.strategystyle = self.selectedstragegy.get_attribute("data-style")  # 选中的策略类型
        self.strategycode = self.selectedstragegy.get_attribute("data-code")  # 选中的策略代码
        self.strategyname = self.selectedstragegy.text  # 选中的策略名称
        logging.info("当前策略：%s_%s"%(self.selectedStrategyName,self.strategycode))
        return  self.strategycode

    def get_navinfo(self):
        """页面净值数据"""
        logging.info("基金净值")
        self.driver.execute_script(StrategyPage._js_totop)  # 返回顶部
        self.getscreenshot("净值")
        navinfo = self.getelements(*StrategyPage._navinfo_locator)  # 净值模块
        nav = self.getchild(navinfo[0],*StrategyPage._h1_locator).text  # 净值
        navDate = self.getchild(navinfo[0],*StrategyPage._p_locator).text[-6:-1]  # 净值日期
        navChange = self.getchild(navinfo[1],*StrategyPage._span_loacator).text[:-1]  # 净值日涨幅
        annualChangeAll = self.getchild(navinfo[2],*StrategyPage._span_loacator).text[:-1]  # 年化回报
        self.navlist = [float(nav), navDate, float(navChange), float(annualChangeAll)]
        return self.navlist

    def get_percents(self):
        """页面组合涨幅数据"""
        self.driver.execute_script(StrategyPage._js_percents) #显示到页面
        logging.info("组合涨幅")
        self.getscreenshot("组合涨幅")
        self.percents_list = []
        groupRiseTbody = self.getelement(*StrategyPage._groupRiseTbody_locator)
        trlist = self.getchilds(groupRiseTbody,*StrategyPage._tr_locator) #获取组合涨幅的数据
        trlen = len(trlist)
        for i in range(trlen):
            tdlist = self.getchilds(trlist[i],*StrategyPage._td_locator)
            tddatalist = [ele.text.replace('%','') for ele in tdlist] #取出值并去掉%
            for i in range(len(tddatalist)): #转化成浮点数
                try:
                    tddatalist[i] = float(tddatalist[i])
                except:
                    pass #不能转化成浮点的忽略
            self.percents_list.append(tddatalist)
        return self.percents_list

    def get_actived_pattern(self):
        """获取当前选中的定投方式"""

        pattern = self.getelement(*StrategyPage._pattern_locator)
        self.pattern = pattern.get_attribute("data-type")
        return  self.pattern

    def get_actived_peroid(self):
        """获取当前选中的投资期限"""

        peroid = self.getelement(*StrategyPage._peroid_locator)
        self.peroid = peroid.get_attribute("data-type")
        return self.peroid

    def choose_style(self,styleindex):
        """选择策略风格"""
        strategyListdt = self.getelement(*StrategyPage._name_locator) # 找到当前所选策略
        self.driver.execute_script(StrategyPage._js_totop) #返回顶部
        strategyListdt.click()  # 点击显示下拉列表
        self.wait(0.5)
        strategystylelist = self.getelements(*StrategyPage._strategystyle_locator)  # 下拉框选项列表
        selectstrategy = strategystylelist[styleindex]
        self.selectStrategystyle = selectstrategy.get_attribute("data-style") # 选择的类型
        self.selectStrategyName = selectstrategy.text # 选择的stylename
        selectstrategy.click()  # 点击风格
        self.wait(1)

    def check_chooseresult(self):
        """验证选择的类型与页面显示类型一致"""
        if self.selectedStrategyName == self.selectStrategyName and self.strategystyle == self.selectStrategystyle:
            return True

    def choose_level(self,levelindex):
        """选择策略级别"""
        strategylevellist = self.getelements(*StrategyPage._strategylevel_locator)  # 策略子类型列表
        self.strategylevellist = [item for item in strategylevellist if item.is_displayed()] #移除不显示的元素
        strategylevel = self.strategylevellist[levelindex]
        strategylevel.click() #点击策略子类型
        self.wait(1)
        return

    def choose_strategy(self,styleindex,levelindex):
        """选择策略风格和级别并获取策略信息"""
        self.choose_style(styleindex) # 选择策略风格
        self.choose_level(levelindex) # 选择级别
        self.get_strategyinfo()  # 选择后获取信息
        styleinfo = "益策略选择S00%s00%s"%(styleindex+1,levelindex+1)
        self.getscreenshot(styleinfo)
        logging.info(styleinfo)

    def choose_trends_pattern(self,patternindex):
        """选择组合走势的定投方式"""
        self.driver.execute_script(StrategyPage._js_trends) #定投方式显示到界面，否则无法点击
        self.patternlist = self.getelements(*StrategyPage._patterns_locator)  # 定投方式
        patternele = self.patternlist[patternindex]
        patternele.click()  # 选择定投方式
        self.wait(1)
        self.pattern = patternele.get_attribute("data-type") #获取定投方式K，W
        self.peroidlist = self.getelements(*StrategyPage._peroids_locator) #获取时间区间

    def choose_trends_peroid(self,peroidindex):
        """选择投资期限，获取组合走势开始日期和业绩表现数据"""
        peroidele = self.peroidlist[peroidindex]
        peroidele.click() # 点击时间区间
        self.wait(2)
        self.peroid = peroidele.get_attribute("data-type") #时间区间
        self.get_trends()
        #log和截图
        trendinfo = "组合走势{pattern}_{peroid}".format(pattern=self.pattern,peroid=self.peroid)
        logging.info(trendinfo)
        self.getscreenshot(trendinfo)


    def get_trends(self):
        """获取组合走势起始日期和业绩表现页面数据"""
        self.startdate = self.getelement(*StrategyPage._startdate_locator).text  # 起始日期
        strategycode = self.get_code()

        """业绩表现页面数据"""
        self.spchartType = self.getelement(*StrategyPage._spchart_locator).text #周期
        self.percentRun = self.getelement(*StrategyPage._percentRun_locator).text #收益率超出、跑输
        self.percentDiff = float(self.getelement(*StrategyPage._percentDiff_locator).text[:-1]) #收益率与业绩基准比较的绝对值
        self.yieldp = float(self.getelement(*StrategyPage._yield_locator).text[:-1]) #收益率
        mdStart_End = self.getelement(*StrategyPage._mdStartEnd_locator).text #最大回撤区间
        self.mdstart = mdStart_End[:10].replace('/', '-') #转化成与接口一样的格式
        self.mdend = mdStart_End[-10:].replace('/', '-') #转化成与接口一样的格式

        self.maxretrace = float(self.getelement(*StrategyPage._maxretrace_locator).text[:-1]) #最大回撤
        self.sharpeRun = self.getelement(*StrategyPage._sharpeRun_locator).text #夏普超出、跑输
        self.sharpeDiff = float(self.getelement(*StrategyPage._sharpeDiff_locator).text[:-1]) #夏普比率比较绝对值
        self.xpRate = self.getelement(*StrategyPage._xpRate_locator).text[:-1] #夏普比率
        try:
            self.xpRate = float(self.xpRate) # 有数值转换，无数值不转换
        except:
            pass

        result = [strategycode,self.startdate, self.percentRun, self.percentDiff, self.yieldp,self.maxretrace,self.sharpeRun,
                  self.sharpeDiff, self.xpRate, self.mdstart,self.mdend]
        return result

    def get_strategy_adjustdate(self):
        """获取策略配置调仓日期"""
        self.selAdjustDatesselect = Select(self.getelement(*StrategyPage._adjustdate_locator)) #调仓日期选择框
        self.adjustDate = self.selAdjustDatesselect.first_selected_option.text #当前选中的日期
        self.adjustDatelist = [opt.get_attribute("value") for opt in self.selAdjustDatesselect.options] #取出所有的调仓日期
        return self.adjustDate

    def choose_adjustdate(self,adjustdate):
        """选择调仓日期并获取配置"""
        self.driver.execute_script(StrategyPage._js_adjustdate) #调仓日期显示到页面
        self.selAdjustDatesselect.select_by_value(adjustdate) #选择调仓日期
        self.wait(0.5)
        #log和截图
        infos = "{adjustdate}配置".format(adjustdate=adjustdate)
        logging.info(infos)
        self.getscreenshot(infos)

    def get_strategy_settings(self):
        """ 获取页面策略配置数据"""
        self.samples = []
        strategyinfo = self.getelement(*StrategyPage._strategyinfo_locator) #策略信息模块
        self.memo = self.getchild(strategyinfo,*StrategyPage._memo_locator).text #memo
        strategydetails = self.getchilds(strategyinfo,*StrategyPage._details_locator) #策略配置列表
        for dl in strategydetails:
            parenttype = self.getchild(dl,*StrategyPage._span_loacator).text #配置大项
            ddlist = self.getchilds(dl,*StrategyPage._dd_locator) #配置子项
            for dd in ddlist:
                sample = [parenttype]
                childtypelist = self.getchilds(dd,*StrategyPage._span_loacator)
                childtype = childtypelist[0].text #子项代码和名称
                name,ticker= childtype.split(" ") #按空格划分
                sample += [ticker,name]
                sample.append(float(childtypelist[1].text[:-1])) #子项权重
                self.samples.append(sample)
        self.samples = sorted(self.samples)
