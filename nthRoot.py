def nth_root(n):
    def actual_root(x):
        root = x ** (1/n)
        return root
    return actual_root

print(nth_root(3)(27))