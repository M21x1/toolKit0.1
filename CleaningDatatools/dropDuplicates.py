import pandas as pd

productions = pd.read_csv('productions.csv')

# Removing complete duplicates

print(productions.drop_duplicates()['title'])