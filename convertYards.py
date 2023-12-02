def convert_yards(y, feet=True):
    if feet is True:
        new_y = y * 3
    else:
        new_y = y * 36
    return new_y

print(convert_yards(10))