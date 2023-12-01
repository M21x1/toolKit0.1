def celsius(x):
    """Converts the temperature from Fahrenheit to Celsius."""
    y = ( x - 32  ) * 5 / 9
    return y

print(celsius(65))