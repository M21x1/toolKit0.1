import pandas as pd
import numpy as np

label_ranges = [1970, 2000, 2010, np.inf]
label_names = ['Pre-millenium', 'Early-2000s', 'Recent']

movies = pd.read_csv('movies.csv')

movies['labels'] = pd.cut(movies['release_year'], bins = label_ranges, labels=label_names)

print(movies[['title','labels']].head())