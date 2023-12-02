letters = ['A', 'B', 'C']
pairs = []
for letter in letters:
    for num in range(0,2):
        pairs.append((letter, num))

pairss = [(letter, num) for letter in letters for num in range(0, 2)]

print(pairss)