def mean(*x):
    """Returns the mean of all the numbers."""
    total_sum = 0
    n = len(x)
    for i in x:
        total_sum = total_sum + i
    return total_sum/n


print((mean(4,5), mean(40, 50 , 45)))