print("Temperature scale converter")
def menu():
    print('''[1] Celsius scale
    [2] Farenheit scale
    [3] Kelvin scale
    [4] Exit''')
    Opt = input("Choose a temperature scale ( 1,2,3 ): ")
    if Opt == "1":
        print("CELSIUS SCALE")
        temperature_celsius = input("Enter the temperature in Celsius scale: ")
        temperature_farenheit = float(temperature_celsius) * 1.8 + 32
        temperature_kelvin = float(temperature_celsius) + 273.15
        print(f'The temperature in celsius scale is {temperature_celsius} degrees')
        print(f'The temperature in farenheit scale is {temperature_farenheit} degrees')
        print(f'The temperature in kelvin scale is {temperature_kelvin} K')
        Opt2 = input("Do you want to continue ( Y/n ): ")
        Opt2.lower()
        if Opt2 == "y":
            menu()

        elif Opt2 == "n":
            exit(0)

        else:
            print("Please answer Y / n")

    elif Opt == "2":
        print("FARENHEIT SCALE")
        temperature_farenheit = input("Enter the temperature in farenheit scale: ")
        temperature_celsius = (float(temperature_farenheit) - 32) * 0.555555555555556
        temperature_kelvin = float(temperature_celsius) + 273.15
        print(f'The temperature in farenheit scale is {temperature_farenheit} degrees')
        print(f'The temperature in celsius scale is {temperature_celsius} degrees')
        print(f'The temperature in kelvin scale is {temperature_kelvin} K')
        Opt2 = input("Do you want to continue ( Y/n ): ")
        Opt2.lower()
        if Opt2 == "y":
            menu()

        elif Opt2 == "n":
            exit(0)

        else:
            print("Please answer Y / n")

    elif Opt == "3":
        print("KELVIN SCALE")
        temperature_kelvin = input("Enter the temperature in kelvin scale: ")
        temperature_celsius = float(temperature_kelvin) - 273.15
        temperature_farenheit = float(temperature_celsius) * 1.8 + 32
        print(f'The temperature in kelvin scale is {temperature_kelvin} K')
        print(f'The temperature in celsius scale is {temperature_celsius} degrees')
        print(f'The temperature in farenheit scale is {temperature_farenheit} degrees')
        Opt2 = input("Do you want to continue ( Y/n ): ")
        Opt2.lower()
        if Opt2 == "y":
            menu()

        elif Opt2 == "n":
            exit(0)

        else:
            print("Please answer Y / n")


    elif Opt == "4":
        exit(0)

    else:
        print("Please enter a number from 1-4")


menu()