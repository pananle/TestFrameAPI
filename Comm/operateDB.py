# 数据库操作模块
# -*- coding:utf-8 -*-

import pymysql
from Conf.config import DB

"""
# host = sql_cfg['host']
# print(host)
# port = sql_cfg['port']
# print(port)
# user = sql_cfg['user']
# print(user)
# pwd = sql_cfg['pwd']
# print(pwd)
# database = sql_cfg['database']
# print(database)
# charset = sql_cfg['charset']
# print(charset)
# 
# try:
#     #连接数据库
#     db = pymysql.connect(host=host, port=int(port), user=user, password=pwd, database=database, charset=charset)
#     #获取游标
#     cursor = db.cursor()
#     #执行SQL
#     cursor.execute("select * from br_id_two_check where ID = '6255';")
#     #获取查询结果
#     result = cursor.fetchall()
#     #打印查询结果
#     print(result)
#     print('执行成功')
# except Exception as e:
#     print('连接失败，原因：{}'.format(str(e)))
"""
"""
封装mysql操作
"""
class OpeartorDB(object):
    def __init__(self):
        """
        初始化方法，习惯性留着
        """
        pass

    def connectDB(self):
        """
        连接数据库
        :return: 返回成功失败，原因
        """
        host = sql_cfg['host']
        port = sql_cfg['port']
        user = sql_cfg['user']
        pwd = sql_cfg['pwd']
        database = sql_cfg['database']
        charset = sql_cfg['charset']


        try:
            self.db = pymysql.connect(host=host, port=int(port), user=user, password=pwd, database=database, charset=charset)
            return True, '连接数据成功'
        except Exception as e:
            return False, '连接数据失败【' + str(e) + '】'


    def closeDB(self):
        """
        关闭数据连接，不关闭会导致数据连接数不能释放，影响数据库性能
        :return:
        """
        self.db.close()

    def excetSql(self, enpsql):
        """
        执行sql方法，
        :param enpsql: 传入的sql语句
        :return: 返回成功与执行结果 或 失败与失败原因
        """
        isOK, result = self.connectDB()
        if isOK is False:
            return isOK, result
        try:
            cursor = self.db.cursor()
            cursor.execute(enpsql)
            res = cursor.fetchone()  # 为了自动化测试的速度，一般场景所以只取一条数据
            if res is not None and 'select' in enpsql.lower():  # 判断是不是查询，
                des = cursor.description[0]
                result = dict(zip(des, res))  # 将返回数据格式化成JSON串
            elif res is None and ('insert' in enpsql.lower() or 'update' in enpsql.lower()):  # 判断是不是插入或者更新数据
                self.db.commit()  # 提交数据操作，不然插入或者更新，数据只会更新在缓存，没正式落库
                result = ''  # 操作数据，不需要返回数据
            cursor.close()  # 关闭游标
            self.closeDB()  # 关闭数据连接
            return True, result
        except Exception as e:
            return False, 'SQL执行失败,原因：[' + str(e) + ']'





sql = 'select * from br_id_two_check where ID = "6225"'
#sql = 'UPDATE `test`.`br_id_two_check` SET `ID` = "6225",`ID_CARD` = "452122198404100339",`NAME` = "韦勇",`IPHONID` = "13416077284" WHERE	`ID` = "6224"	AND `ID_CARD` = "452122198404100338" AND `NAME` = "韦其勇" AND `IPHONID` = "13416077283"'
oper = OpeartorDB()
isOK, result = oper.excetSql(sql)
print(result)
