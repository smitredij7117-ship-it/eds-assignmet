import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)
# write the code
date_groups = df.groupby('Date')['Product'].apply(list)

pair_counter = Counter()

for products in date_groups:
    unique_pairs = combinations(sorted(set(products)), 2)
    pair_counter.update(unique_pairs)

max_freq = max(pair_counter.values())

for pair, count in pair_counter.items():
    if count == max_freq:
       print(f"{pair[0]} and {pair[1]}: {count} times")

# Output the most frequent product pairs