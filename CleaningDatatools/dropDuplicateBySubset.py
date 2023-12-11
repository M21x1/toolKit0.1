import pandas as pd

df = pd.read_csv('productions.csv')

df = df[df.duplicated(
    subset=['title', 'country'], keep= 'first'
)]

print(df)