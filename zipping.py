characters_names = ['Felicity Smoak', 'Laurel Lance']
code_names = ['Overwatch', 'Black Canary']

team_arrow = zip (characters_names, code_names)

for i, j in team_arrow:
    print(i + ' is The ' + j)