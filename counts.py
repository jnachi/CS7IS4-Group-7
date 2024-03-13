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
output_directory = './data'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Create CSV with all uni-gram frequency counts and seperate CSV with all bi-gram frequency counts
df_all_uni = pd.DataFrame()
df_all_bi = pd.DataFrame()
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        print(f"Counting {filename} ...")

        input_path = os.path.join(input_directory, filename)
        
        with open(input_path, 'r', encoding='utf-8') as file:
            uni_grams = json.load(file)
            
        # Generate bi-grams
        bi_grams = [word1+' '+word2 for word1, word2 in zip(uni_grams[:-1], uni_grams[1:])]
            
        # Count frequency of uni-grams
        df_uni = pd.DataFrame(Counter(uni_grams), index=[0])
        df_uni["filename"] = filename
        df_all_uni = pd.concat([df_all_uni, df_uni])
        
        # Count frequency of bi-grams
        df_bi = pd.DataFrame(Counter(bi_grams), index=[0])
        df_bi["filename"] = filename
        df_all_bi = pd.concat([df_all_bi, df_bi])
        
    
df_all_uni = df_all_uni.fillna(0)
df_all_uni.to_csv(os.path.join(output_directory, 'all_uni-grams.csv'), index=False)
    
df_all_bi = df_all_bi.fillna(0)
df_all_bi.to_csv(os.path.join(output_directory, 'all_bi-grams.csv'), index=False)
