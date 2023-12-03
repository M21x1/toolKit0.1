code_names = ['Spartan', 'Green Arrow']

characters_names = ['John Diggle', 'Oliver Queen']

team_arrow = zip(code_names, characters_names)

# Unpacking!!!

cnames, names = zip(*team_arrow)

# Print only the names

print(names)