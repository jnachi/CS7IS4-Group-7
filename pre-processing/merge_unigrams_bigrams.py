#Python script to Merge the CSV files with Unigrams and Bigrams frequency

import pandas as pd

df_uni_grams = pd.read_csv('data/uni-grams_rel-frequ.csv')
df_bi_grams = pd.read_csv('data/bi-grams_rel-frequ.csv')


df_universities = pd.read_csv('university_list_combined.csv')  

merged_df = pd.merge(df_universities, df_uni_grams, on='filename', how='left')
merged_df = pd.merge(merged_df, df_bi_grams, on='filename', how='left')

merged_df.fillna(0, inplace=True)
merged_df.to_csv('features_n-grams_merged.csv', index=False)
