# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:25:33 2022

@author: gche0026
"""


import pandas as pd
import numpy as np

def stringCut(string):
    return string[6:10]

df1 = pd.read_csv('C:/Users/gche0026/Downloads/Downloads/2001.csv', index_col=0,error_bad_lines=False)
df2 = pd.read_csv('C:/Users/gche0026/Downloads/Downloads/2005.csv', index_col=0,error_bad_lines=False)
df3 = pd.read_csv('C:/Users/gche0026/Downloads/Downloads/2008.csv', index_col=0,error_bad_lines=False)
df4 = pd.read_csv('C:/Users/gche0026/Downloads/Downloads/2012.csv', index_col=0,error_bad_lines=False)

df = df1
df = df.append(df2, ignore_index=True)
df = df.append(df3, ignore_index=True)
df = df.append(df4, ignore_index=True)
print("df attained - tinme to reduce the entries")

df['Date'] = df['Date'].apply(stringCut)
print("date string cut time to cut redundant column entries")


df_out1 = df[['Date', 'Primary Type','Latitude','Longitude']]
print("df1 entries cut - tinme to cut df2")
df_out2 = df[['Date', 'Community Area']]
print("df2 entries cut - tinme to write csv")



df_out2.to_csv("C:/Users/gche0026/Downloads/Downloads/allYears.csv")
print('csv1 done time to write csv 2')
df_out1.to_csv("C:/Users/gche0026/Downloads/Downloads/allYearsCommunityArea.csv")
