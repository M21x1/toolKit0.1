# We're using the matches variable to replace the typo TVShow in the type column of the prod_types DataFrame

matches = [('TV Show', 100), ('TVShow', 92), ('MOVIE', 31), ('movie', 31), ('Movie', 31)]

for match in matches:
    if match[1] >= 80: 
        prod_types.loc[prod_types['type'] == match[0]] = 'TV Show'

print(prod_types['type'].head())