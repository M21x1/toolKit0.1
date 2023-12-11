import pandas as pd

fix = 'September 17, 2021'
bug = 'September 17, 2029'

tv = pd.read_csv('date_title.csv')

print(tv.columns)

# Ensure the column name matches your expectations
# If the column name has leading/trailing whitespaces, remove them
tv.columns = tv.columns.str.strip()

# Print the DataFrame to verify its structure
print(tv)


tv.loc[tv['date'] == bug, 'date'] = [fix]
tv['date'] = pd.to_datetime(tv['date']).dt.date

print(tv['date'].max())