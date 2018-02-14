"""Read dataset_a

More description if relevant...
"""
import pandas as pd

df = pd.read_csv('data/raw/dataset_a')

df.to_hdf('data/processed/dataset_a.h5', 'dataset_a')

# read in from another script
df1 = pd.read_hdf('data/processed/dataset_a.h5', 'dataset_a')

print(df.head())
