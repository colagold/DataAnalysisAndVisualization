# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 9:16
# @Author  : colagold
# @FileName: pickles.py
import pickle

class People:
    def __init__(self):
        self.id=0
        self.age=10

    def get_age(self):
        return self.age

p=People()
# 序列化对象
data = {'people':p,'name': 'John', 'age': 30}
with open('../output/txt/data.pkl', 'wb') as file:
    pickle.dump(p, file)

# 反序列化对象
with open('../output/txt/data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)

