import pandas as pd
import os
'''
    总结pandas中利用DataFrame进行文件转换
'''
def file_convert(path):
    df= pd.read_table(path, header=None)
    df.to_csv("test.csv",header=False,index=False) # 只保存数据主体，不保存索引列合头