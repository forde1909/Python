#Temperature conversion program

print("Welocme to the Temperature conversation program: \n")

#Collect temperature from the user
temp = float(input("Enter your given temperature in degrees Ferhareint: "))

#convert temp to Celcius and Kelvin
temp_cel = (temp - 32) * 5/9
temp_kel = (temp - 32) * 5/9 + 273.15

#Round temps
temp = round(temp,4)
temp_cel = round(temp_cel,4)
temp_kel = round(temp_kel,4)

#Display results to the user
print("Degrees Fahrenheit: \t" + str(temp))
print("Degress Celcius: \t" + str(temp_cel))
print("Degress Kelvin: \t" + str(temp_kel))

print("Your " + str(temp) + " °F is " + str(temp_cel) + " Celcius")
print("Your " + str(temp) + " °F is " + str(temp_kel) + " Kelvin")
