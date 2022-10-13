# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 01:42:34 2022

@author: gche0026
"""


import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/gche0026/OneDrive/Documents/GitHub/FIT3179-Visualisation-2/data/racial-crime/fatal_encounters_dot_org.csv', index_col=False,error_bad_lines=False)

df = df[['Date (Year)','Location of death (state)']]

state_array = ['GA','IL','HI','IN','TN','LA','UT']


df_out = df.loc[df['Location of death (state)']=='GA']

for i in range(len(state_array)-1):
    df_next = df.loc[df['Location of death (state)']==state_array[i+1]]
    df_out = df_out.append(df_next)

df_out.to_csv("C:/Users/gche0026/OneDrive/Documents/GitHub/FIT3179-Visualisation-2/data/fatalitiesData.csv",index=False)