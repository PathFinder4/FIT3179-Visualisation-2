# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 01:39:53 2022

@author: gche0026
"""

import pandas as pd
import numpy as np


df = pd.read_csv('C:/Users/gche0026/OneDrive/Documents/GitHub/FIT3179-Visualisation-2/data/unprocessedData/1975-2015-crime.csv', index_col=False,error_bad_lines=False)
city_array = ['Albuquerque','Atlanta','Boston','Charlotte','Chicago','Dallas','Denver','Detroit','Fairfax County','Honolulu','Indianapolis','Jacksonville','Kansas City','Las Vegas','Los Angeles','Louisville','Memphis','Milwaukee','Minneapolis','Montgomery County','New Orleans','New York City','Newark','Oklahoma City','Omaha','Philadelphia','Phoenix','Salt Lake City','Seattle','Washington','Wichita']
city_array_highlight = ['Atlanta','Chicago','Honolulu','Indianapolis','Memphis','New Orleans','Salt Lake City']

df_out = df.loc[df['agency_jurisdiction']=='Albuquerque']
df_out2 = df.loc[df['agency_jurisdiction']=='Atlanta']

for i in range(len(city_array)-1):
    df_next = df.loc[df['agency_jurisdiction']==city_array[i+1]]
    df_out = df_out.append(df_next)
    
for i in range(len(city_array_highlight)-1):
    df_next = df.loc[df['agency_jurisdiction']==city_array_highlight[i+1]]
    df_out2 = df_out2.append(df_next)

years = range(1975,2016)
for year in years:
    df_year = df_out.loc[df_out['report_year']==year]
    df_year.to_csv("C:/Users/gche0026/OneDrive/Documents/GitHub/FIT3179-Visualisation-2/data/overviewYear/{}.csv".format(year))
    


df_out.to_csv("C:/Users/gche0026/OneDrive/Documents/GitHub/FIT3179-Visualisation-2/data/overViewData.csv")
df_out2.to_csv("C:/Users/gche0026/OneDrive/Documents/GitHub/FIT3179-Visualisation-2/data/yearlyOverview.csv")
# import csv

# with open('C:/Users/gche0026/OneDrive/Documents/GitHub/FIT3179-Visualisation-2/data/1975-2015-crime.csv', newline='') as csvfile:
#     data = list(csv.reader(csvfile))

# year = 1975
# for i in range(2015-1975):
#     current_year = year+i
#     next_year = current_year+1
#     i = 0
#     while data[i] 
    