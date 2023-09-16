
import pandas as pd
from datetime import datetime
file_name='Amazon_Digital_Music'
path = 'E:\Resourse\研究生\模型\OpinionGCN\数据集\{}\{}.inter'.format(file_name,file_name)


df=pd.read_table(path)
print("读取所有数据成功")

#过滤：筛选交互次数小于五次的用户
user_fre=df["user_id:token"].value_counts()
df=df[~df["user_id:token"].isin(user_fre[user_fre<5].index)]

print(f'{file_name} users:{df["user_id:token"].unique().shape[0]}')
print(f'{file_name} items:{df["item_id:token"].unique().shape[0]}')
# 记录开始时间
start_time = datetime.now()
# 映射表
user_id = df["user_id:token"].unique()
user_dic=dict(zip(user_id, [i + 1 for i in range(user_id.shape[0])]))

item_id = df["item_id:token"].unique()
item_dic=dict(zip(item_id, [i + 1 for i in range(item_id.shape[0])]))
time1 = datetime.now()
print("建立映射表成功,耗时:",time1-start_time)


df.iloc[:,0].replace(user_dic,inplace=True)
df.iloc[:,1].replace(item_dic, inplace=True)
df.to_csv("{}.csv".format(file_name),header=False, index=False)

# for i,d in enumerate(df_chunk):
#     d.iloc[:,0].replace(user_dic,inplace=True)
#     time2 = datetime.now()
#     print("user id替换成功,耗时:", time2 - time1)
#     d.iloc[:,1].replace(item_dic, inplace=True)
#     d.to_csv("epinions.csv", mode='a',header=False, index=False)
time2 = datetime.now()
print("替换成功,耗时:",time2-time1)
#     total.add(d)


