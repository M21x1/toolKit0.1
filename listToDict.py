def list_to_dict(x, y):
    lists = zip (x, y)
    new_dict = dict(lists)
    return new_dict


a = ['a', 'b', 'c']

b = [12, 15, 18]

print(list_to_dict(a,b))