
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