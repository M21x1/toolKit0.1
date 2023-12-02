def square(s):
    """Returns area & perimeter of a square."""
    try:
        a = s * s
        p = 4 * s
        return a, p
    except TypeError:
        print('s can not be a string.')
        

square('5')  