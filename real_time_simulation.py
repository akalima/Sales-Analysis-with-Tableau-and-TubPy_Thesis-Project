import pandas as pd
import time
import random
import os

df = pd.read_csv('FactSales_cleaned.csv', sep=';')
print(df.head())

# Check if the live-copy already exists
if os.path.exists('FactSales.csv'):
    os.remove('FactSales.csv')

# The main part for the visualizations at launch
df.iloc[:170000].assign(BatchID=0).to_csv('FactSales.csv', index=False, sep=';')

i = 170000
batch_id = 1

while i < len(df):
    # Choose lines to add
    num_of_lines = random.randint(20, 50)
    new_lines = df.iloc[i:i+num_of_lines].copy()
    new_lines.loc[:, 'BatchID'] = batch_id

    # Add lines to the .csv
    new_lines.to_csv('FactSales.csv',
                    mode='a',   # append (not rewrite)
                    header=not os.path.exists('FactSales.csv'),   # if the file is new, create headers
                    index=False,    # no pandas indexes
                    sep=';')

    # Show the result
    print(f'Added rows ({num_of_lines}) with BatchID={batch_id}: {i+num_of_lines}/{len(df)}')

    i += num_of_lines
    batch_id += 1

    # pauses between the iterations
    time.sleep(random.uniform(2, 5))
