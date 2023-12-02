# Generator function that loads data in chunks.

def read_large_file(file_object):
    """A generator function to read a large file lazily."""
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data # yield makes this function a generator function.

print(read_large_file('googlemapsas.csv'))