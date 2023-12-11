import pandas as pd

data = {'movie':[2,2], 'year':[1980,1980]}


df = pd.DataFrame(data)

df = df[df.duplicated()]

print(df)
