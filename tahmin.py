# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:24:08 2024

@author: feridun
"""

# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler=pd.read_csv("veriler.csv")

print(veriler)

all_boy=veriler[["boy"]]

print(all_boy)

from sklearn.impute import SimpleImputer

imputer=SimpleImputer(missing_values=np.nan,strategy="mean")

yas=veriler.iloc[:,1:4].values
imputer=imputer.fit(yas[:,1:4])
yas[:,1:4]=imputer.transform(yas[:,1:4])

ulke=veriler.iloc[:,0:1].values

from sklearn import preprocessing

le=preprocessing.LabelEncoder()

ulke[:,0]=le.fit_transform(veriler.iloc[:,0])
print(ulke)

cinsiyet = veriler.iloc[:, -1:].values
cinsiyet[:, 0] = le.fit_transform(veriler.iloc[:, -1])

print(cinsiyet)

ohe=preprocessing.OneHotEncoder()
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)

output=pd.DataFrame(data=ulke,index=range(7),columns=["abd","tr","uk"])
print(output)

output2=pd.DataFrame(data=yas,index=range(7),columns=["boy","kilo","yas"])
print(output2)

output3=pd.DataFrame(data=cinsiyet,index=range(7),columns=["cinsiyet"])
print(output3)

data_set=pd.concat([output,output2], axis=1)

data_set2=pd.concat([data_set,output3], axis=1)
print(data_set2)

from sklearn.model_selection import train_test_split

x_train , x_test , y_train, y_test = train_test_split(data_set,output3,test_size=0.33,random_state=0)   
          
from sklearn.preprocessing import LabelEncoder

# LabelEncoder'ı kullanarak kategorik veriyi sayısal hale getirme
le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train)

# Modeli eğitme


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train, y_train_encoded)

y_pred = regressor.predict(x_test)

boy=data_set2.iloc[:,3:4].values
print(boy)
left=data_set2.iloc[:,:3]
right=data_set2.iloc[:,4:]
veri=pd.concat([left,right],axis=1)

x_train , x_test , y_train, y_test = train_test_split(veri,boy,test_size=0.33,random_state=0) 

y_train_encoded = le.fit_transform(y_train)



r2=LinearRegression()
r2.fit(x_train,y_train_encoded)

y_pred=r2.predict(x_test)  

import statsmodels.api as sm

row_count = veri.shape[0]
X = np.append(arr=np.ones((row_count, 1)).astype(int), values=veri, axis=1)

X_1=veri.iloc[:,[0,1,2,3,4,5]].values

X_1=np.array(X_1,dtype=float)
model=sm.OLS(boy,X_1).fit()
print(model.summary())

X_1=veri.iloc[:,[0,1,2,3]].values

X_1=np.array(X_1,dtype=float)
model=sm.OLS(boy,X_1).fit()
print(model.summary())


























