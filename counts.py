# -*- coding: utf-8 -*-
"""
Read tokens and performs the following pre-processing steps:
    - count the frequency of uni- and bi-grams
    - calculate the relative frequencies

TODOs:
    - concat uni- and bi-gram dataframes
    - add a column with file name to be able to join with metadata
    - iterate over all files and generate a single CSV
    
Next steps:
    - look at most common uni- and bi-grams and decide on thresholds for filtering
      to reduce dimensionality

@author: K. Nolle
"""


import re
from collections import Counter
import pandas as pd
import os
import json


input_directory = './data/tokenized-txt'
filename = '2018_UBC_Strategic_Plan_Full-20180425.txt'

input_path = os.path.join(input_directory, filename)

with open(input_path, 'r', encoding='utf-8') as file:
    uni_grams = json.load(file)
    

# Count and calculate relative frequency of uni-grams
df_uni = pd.DataFrame(Counter(uni_grams), index=[0])
df_uni = df_uni.div([len(uni_grams)], axis=0)

# Generate bi-grams
bi_grams = [word1+' '+word2 for word1, word2 in zip(uni_grams[:-1], uni_grams[1:])]

# Count and calculate relative frequency of bi-grams
df_bi = pd.DataFrame(Counter(bi_grams), index=[0])
df_bi = df_bi.div([len(bi_grams)], axis=0)

print(df_bi)