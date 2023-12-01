def add_zeros(string):
    """Returns a string padded with zeros to ensure consistent length."""
    updated_string = string + '0'
    def add_more():
        """Adds more zeros if necessary."""
        nonlocal updated_string
        updated_string = updated_string + '0'
    while len(updated_string) < 6:
        add_more()
    return updated_string

print(add_zeros('3.6'), add_zeros('5.7'))