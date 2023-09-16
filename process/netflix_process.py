import pandas as pd

file_name='netflix'
path = 'E:\Resourse\研究生\模型\OpinionGCN\数据集\{}\{}.inter'.format(file_name,file_name)

df = pd.read_table(path, header=None, delimiter='\\s',engine='python',encoding='utf-8')

#过滤：筛选交互次数小于五次的用户
user_fre=df[0].value_counts()
df=df[~df[0].isin(user_fre[user_fre<5].index)]

print(f'{file_name} users:{df[0].unique().shape[0]}')
print(f'{file_name} items:{df[1].unique().shape[0]}')

df=df[~df[1].isin(user_fre[user_fre<5].index)]

print(f'{file_name} users:{df[0].unique().shape[0]}')
print(f'{file_name} items:{df[1].unique().shape[0]}')