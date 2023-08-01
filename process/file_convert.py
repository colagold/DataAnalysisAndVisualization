import pandas as pd
import numpy as np
import scipy.sparse as sp
import os
'''
    总结pandas中利用DataFrame进行文件转换
'''
def file_convert(path):
    #df= pd.read_table(path, header=None, delimiter='\\s',engine='python',encoding='utf-8')
    df=pd.read_csv(path,header=None)
    df.to_csv("ratings.csv",header=False,index=False) # 只保存数据主体，不保存索引列合头

    uids = df.iloc[:, 0].values
    iids = df.iloc[:, 1].values
    rates = df.iloc[:, 2].values
    ds = sp.csr_matrix((rates, (uids, iids))
                       , dtype=np.float32)

file_convert("../output/txt/Coat.txt")