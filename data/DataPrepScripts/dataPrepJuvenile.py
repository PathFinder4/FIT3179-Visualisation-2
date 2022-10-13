# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 01:42:06 2022

@author: gche0026
"""

import pandas as pd
import numpy as np

df1 = pd.read_csv('C:/Users/gche0026/OneDrive/Documents/GitHub/FIT3179-Visualisation-2/data/unprocessedData/arrests_national_juvenile.csv', index_col=0,error_bad_lines=False)
df2 = pd.read_csv('C:/Users/gche0026/OneDrive/Documents/GitHub/FIT3179-Visualisation-2/data/unprocessedData/juv_pop.csv', index_col=0,error_bad_lines=False)

df_out = df.loc[df['year']=='Albuquerque']

#not used unfinished just did it on excel