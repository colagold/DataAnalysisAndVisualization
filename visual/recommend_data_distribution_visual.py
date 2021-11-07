import torch
import numpy as np
import copy
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import pandas as pd
import os
import scipy.sparse as sp

def parse_data(data_dir):
    fdata = os.path.join(data_dir,'rating.data')
    #=data_dir
    # fdata = os.path.join(data_dir, 'rating.data')
    # df = pd.read_table(fdata,header=None,delimiter='\\s')
    df = pd.read_table(fdata,header=None)
    if df.shape[1] == 1:
        df = pd.read_table(fdata, header=None, delimiter='\\s',engine='python')
    uids = df.iloc[:, 0].values
    iids = df.iloc[:, 1].values
    rates = df.iloc[:, 2].values
    ds = sp.csr_matrix((rates, (uids, iids)),dtype=np.float)  # 参照： csr_matrix((data,  (row_ind, col_ind)), [shape=(M, N)])
    return ds

def draw_plot(ds,ylim=700,title='ml-100k data set score distribution'):
    col = ds.T.tolil().rows  # 获取每个商品的用户集
    item_userset = dict([(i, torch.from_numpy(np.array(col)).long())  # 商品用户集
                         for i, col in enumerate(col)])

    position = [i for i in item_userset]
    data = [item_userset[i].shape[0] for i in item_userset]
    newdata = copy.deepcopy(data)
    newdata.sort(reverse=True)
    plt.title(title)
    y_major_locator = MultipleLocator(100)
    ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    plt.ylim(0, ylim)
    plt.bar(x=position, height=newdata)
    head_length = int(len(position) * 0.2)
    plt.bar(position[:head_length], newdata[:head_length], color='blue', label='popularity')
    plt.bar(position[head_length:], newdata[head_length:], color='red', label='longtail')
    plt.legend()
    plt.ylabel('ratings', fontsize=10)
    plt.xlabel(' item index (sorted by #ratings)', fontsize=10)
    plt.savefig('../output/pic/'+title+".png")
    plt.show()

if __name__=="__main__":
    draw_plot(parse_data("../data/recommend/ml-100k"))