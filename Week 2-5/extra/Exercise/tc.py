temp_kelvin(degree)
    #Converts from kelvin to celsius
    return.round(degree - 273.15, 2)

temp_fahrenheit(degree):
    """Converts from fahrenheit to celsius"""
    return round((degree - 32) * (5 / 9), 2)


# temp_degree = input("What temperature do you want to convert to Celsius?\n Type F or K: ").upper()
 temp_degree = [280, 285, 290, 295, 300, 305, 310, 320, 325, 330]
 
 
 my_temperature_in_celsius = [(temp_kelvin(degree) for temperature in temp_degree]
print(my_temperature_in_celsius)


#temperature_in_kelvin = [280, 285, 290, 295, 300, 305, 310, 320, 325, 330]
#my_temperature_in_celsius = [(temperature - 273.15) for temperature in temperature_in_kelvin]
#print(my_temperature_in_celsius)

#if temp_degree == "F":
 #   temperature = float(input("Type in the temperature number: "))
  #  print(f"The temperature of {temperature}~F is equivalent to {temp_fahrenheit(temperature)}~C")
#if temp_degree == "K":
 #   temperature = float(input("Type in the temperature number: "))
  #  print(f"The temperature of {temperature}~K is equivalent to {temp_kelvin(temperature)}~C")
#else:
 #   print("You have entered an invalid key. Try again!")
