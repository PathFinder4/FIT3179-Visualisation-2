# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:25:33 2022

@author: gche0026
"""


import pandas as pd
import numpy as np

df = pd.read_csv('mm_master_demos.csv', index_col=0)
map_bounds = pd.read_csv('map_data.csv', index_col=0)