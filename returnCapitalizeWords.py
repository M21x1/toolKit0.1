x = ['aPPle', 'baNANa']

def caps(li):
    """Returns a list, with all elements capitalized."""
    def inner(w):
        """Returns a capitalized word."""
        return w.capitalize()
    return ([inner(li[0]), inner(li[1])])


print(caps(x))