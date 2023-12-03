floats = []
integers = []

for float in floats:
    integers.append(round(float))
    
# As a list comprehension:

floats = [9.33, 7.78, 3.16, 6.52]

integers = [ round(x) for x in floats]

print(integers)