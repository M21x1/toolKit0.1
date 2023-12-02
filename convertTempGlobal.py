temp = 15

def convert_temp(x):
    """Converts the temperature from Celsius to Fahrenheit"""
    global temp
    temp = (x*1.8) + 32


convert_temp(temp)

print(temp)