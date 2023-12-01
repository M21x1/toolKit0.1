def rectangle(length, width):
    """Returns the area and perimeter of a rectangle."""
    a = length * width
    p = 2 * (length + width)
    return a, p


area, perimeter = rectangle(36, 12)

print(area, perimeter)