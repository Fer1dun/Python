# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 16:59:45 2024

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

ohe=preprocessing.OneHotEncoder()
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)

output=pd.DataFrame(data=ulke,index=range(7),columns=["abd","tr","uk"])
print(output)

output2=pd.DataFrame(data=yas,index=range(7),columns=["boy","kilo","yas"])
print(output2)

cinsiyet=veriler.iloc[:,-1].values
output3=pd.DataFrame(data=cinsiyet,index=range(7),columns=["cinsiyet"])
print(output3)

data_set=pd.concat([output,output2], axis=1)

data_set2=pd.concat([data_set,output3], axis=1)
print(data_set2)

from sklearn.model_selection import train_test_split

x_train , x_test , y_train, y_test = train_test_split(data_set,output3,test_size=0.33,random_state=0)   
          
#özyineli ölcekleme

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
new_x_train=sc.fit_transform(x_train)
new_x_test=sc.fit_transform(x_test)






















