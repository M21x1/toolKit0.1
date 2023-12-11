import pandas as pd

dat = {'type':['TVShow', 'TVshow'], 'title':['The Great British Baking Show', 'Dear White People']}


df = pd.DataFrame(dat)
df['type'] = df['type'].str.lower()
df['type'] = df['type'].replace({"tvshow":"TV Show"})

print(df)