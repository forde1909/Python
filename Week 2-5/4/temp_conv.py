

temperature_in_kelvin = [280, 285, 290, 295, 300, 305, 310, 320, 325, 330]

my_temperature_in_celsius = [(temperature - 273.15) for temperature in temperature_in_kelvin]


my_temperature_in_fahrenheit = [(temperature - 32) * (5 / 9) for temperature in temperature_in_kelvin]

print("\nTemperature in Celsius :") 
print(my_temperature_in_celsius)
print("\nTemperature in Fahrenheit :") 
print(my_temperature_in_fahrenheit)



