def sorted_elements(x, desc=True, n=2):
    """Returns the n largest or smallest elements of a list."""
    new_x = sorted(x, reverse=desc)[0:n]
    return new_x


a = [0, 6, 11, 1, 0, 10]
print(sorted_elements(a, n=3))