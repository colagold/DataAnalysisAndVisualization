import os
import pandas as pd
from collections import Counter

def is_bad_data(data_dir):
    fdata = os.path.join(data_dir, 'rating.data')
    # =data_dir
    # fdata = os.path.join(data_dir, 'rating.data')
    # df = pd.read_table(fdata,header=None,delimiter='\\s')
    df = pd.read_table(fdata, header=None)
    if df.shape[1] == 1:
        df = pd.read_table(fdata, header=None, delimiter='\\s', engine='python')
    uids = df.iloc[:, 0].values
    iids = df.iloc[:, 1].values
    rates = df.iloc[:, 2].values
    iids_count=Counter(iids) # 字典
    rates_count=Counter(rates)
    u_i_list=list(zip(uids,iids))
    s=set()
    for ele in u_i_list:
        s.add(tuple(ele))
    print("user-item nums:",len(u_i_list))
    print("unique user-item nums:",len(s))
    print(len(u_i_list)-len(s))

def delete_repeat(data_dir):
    fdata = os.path.join(data_dir, 'rating.data')
    # =data_dir
    # fdata = os.path.join(data_dir, 'rating.data')
    # df = pd.read_table(fdata,header=None,delimiter='\\s')
    df = pd.read_table(fdata, header=None)
    if df.shape[1] == 1:
        df = pd.read_table(fdata, header=None, delimiter='\\s', engine='python')
    uids = df.iloc[:, 0].values
    iids = df.iloc[:, 1].values
    rates = df.iloc[:, 2].values
    data_dic=dict()
    u_i_list = list(zip(uids, iids))
    for ele in u_i_list:
        data_dic[tuple(ele)]=rates[u_i_list.index(ele)]
    file=open("../output/txt/filmtrust.txt", 'a+')
    for k,v in data_dic.items():
        file.write(str(k[0])+"\t"+str(k[1])+"\t"+str(v)+"\n")
    file.close()
    #print(data_dic)

if __name__ == "__main__":
    data_dir = "../data/recommend/FilmTrust"
    is_bad_data(data_dir)
    delete_repeat(data_dir)
