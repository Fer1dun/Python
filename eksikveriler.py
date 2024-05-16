# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 21:28:01 2024

@author: feridun
"""


"""
Spyder Editor

This is a temporary script file.
"""
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
print(yas)