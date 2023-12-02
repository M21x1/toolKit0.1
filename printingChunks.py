
# This code prints in chunks. Print the second chunk.

import pandas as pd

chunky = pd.read_csv('googlemapsas.csv', chunksize=4)
next(chunky) # Calls the first chunk
print(next(chunky)) # calls and print the second chunk