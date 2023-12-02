from functools import reduce

product = [10, 1, 4]
result = reduce(lambda x, y: x*y, product)
print(result)