#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 12:27:24 2023

@author: marco.herry
"""

import os
import pandas as pd

# get current directory
current_dir = os.getcwd()

# list to hold dataframes
df_list = []

# iterate through all excel files in the directory
for file in os.listdir(current_dir):
    if file.endswith('.xlsx'):
        # read the excel file
        data = pd.read_excel(file)
        df_list.append(data)

# concatenate all dataframes in the list
result = pd.concat(df_list, ignore_index=True)

# save the concatenated data to a new file
result.to_excel('concatenated_file.xlsx', index=False)