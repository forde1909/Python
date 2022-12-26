def temp_kelvin(degree):
    """Converts from kelvin to celsius"""
    return round(degree - 273.15, 2)


def temp_fahrenheit(degree):
    """Converts from fahrenheit to celsius"""
    return round((degree - 32) * (5 / 9), 2)


temp_degree = input("What temperature do you want to convert to Celsius?\n Type F or K: ").upper()

if temp_degree == "F":
    temperature = float(input("Type in the temperature number: "))
    print(f"The temperature of {temperature}~F is equivalent to {temp_fahrenheit(temperature)}~C")
elif temp_degree == "K":
    temperature = float(input("Type in the temperature number: "))
    print(f"The temperature of {temperature}~K is equivalent to {temp_kelvin(temperature)}~C")
else:
    print("You have entered an invalid key. Try again!")
Print()
