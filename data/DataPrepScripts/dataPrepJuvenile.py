# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 01:42:06 2022

@author: gche0026
"""

import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/gche0026/OneDrive/Documents/GitHub/FIT3179-Visualisation-2/data/unprocessedData/arrests_national_juvenile.csv', index_col=0,error_bad_lines=False)
df2 = pd.read_csv('C:/Users/gche0026/OneDrive/Documents/GitHub/FIT3179-Visualisation-2/data/unprocessedData/juv_pop.csv', index_col=0,error_bad_lines=False)

violent_crime_types = ['Simple Assault', 'Aggravated Assault', 'Murder and Nonnegligent Homicide','Rape', 'Robbery']

df_out = df.loc[df['offense_name']=='Simple Assault']


for i in range(len(violent_crime_types)-1):
    df_next = df.loc[df['offense_name']==violent_crime_types[i+1]]
    df_out = df_out.append(df_next)
    
df3 = df.groupby('Courses').sum()

df_out.to_csv("C:/Users/gche0026/OneDrive/Documents/GitHub/FIT3179-Visualisation-2/data/juvDataSimplified.csv")

#not used unfinished just did it on excel