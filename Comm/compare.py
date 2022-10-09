# 封裝json比較，用于接口测试结果对比
# -*- coding: utf-8 -*-

__author__ = 'Leo'


class CompareStr(object):
    def is_contains(self, str1, str2):
        """
        判断预期结果与实际结果是否相同
        :param str1: 预期结果
        :param str2: 实际结果
        :return flag: 标记
        """
        self.flag = None
        if str1 in str2:
            self.flag = True
        else:
            flag = False
        return self.flag


if __name__ == '__main__':
    cs = CompareStr()
    print(cs.is_contains('123', '123456'))
