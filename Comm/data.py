# 封装测试数据读取方法
# 读取EXCEL实现（data）

import pandas as pd

def read_excel(file, **kwargs):
    data_dict = []
    try:
        data = pd.read_excel(file, **kwargs)
        data_dict = data.to_dict('records')
    finally:
        return data_dict


sheet1 = read_excel('zalyquanma.xlsx')
sheet2 = read_excel('zalyquanma.xlsx', sheet_name='Sheet2')
print(sheet1)
print(sheet2)
