# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:47:48 2024

@author: feridun
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler=pd.read_csv("satis.csv")

print(veriler)

aylar=veriler[["Aylar"]]
print(aylar)

satislar=veriler[["Satislar"]]
print(satislar)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(aylar, satislar, test_size=0.33, random_state=0) 
          
#özyineli ölcekleme
'''
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
new_x_train=sc.fit_transform(x_train)
new_x_test=sc.fit_transform(x_test)

new_y_train=sc.fit_transform(y_train)
new_y_test=sc.fit_transform(y_test)
'''
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train, y_train)

tahmin = lr.predict(x_test)


x_train_np = x_train.values.flatten()
y_train_np = y_train.values.flatten()
x_test_np = x_test.values.flatten()

x_train_np = np.sort(x_train_np)
y_train_np = np.sort(y_train_np)


plt.plot(x_train_np, y_train_np, label='Eğitim Verileri')
plt.plot(x_test_np, tahmin, label='Tahminler')
plt.xlabel('Aylar')
plt.ylabel('Satislar')
plt.legend()
plt.show()
























