#Python script to Merge the CSV files with Unigrams and Bigrams frequency

import pandas as pd

df_uni_grams = pd.read_csv('data/extracted-words/uni-grams_rel-frequ.csv')
df_bi_grams = pd.read_csv('data/extracted-words/bi-grams_rel-frequ.csv')


df_universities = pd.read_csv('Merged_CSV.csv')  

merged_df = pd.merge(df_universities, df_uni_grams, on='filename', how='left')
merged_df = pd.merge(merged_df, df_bi_grams, on='filename', how='left')

merged_df.fillna(0, inplace=True)
merged_df.to_csv('Merged_Data_with_Frequencies.csv', index=False)
