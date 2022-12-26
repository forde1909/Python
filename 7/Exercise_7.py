"""
Joseph Forde
Exercise_7
Student number: L00169708
"""


while True:

    # Fuel in the tank
    fuel_tank = input("\nEnter Volume of fuel in Liters in tank:   ")
    fuel_tank = float(fuel_tank)

    # Fuel Consumption in Liters/Per minute
    fuel_used = float(0.03)

    #Get distance driven from the user
    time_ = input ("\nTime running in minutes:   ")
    time_ = float(time_)


    # Calculate and print the answer
    fuel_consumed = fuel_used * time_
    fuel_remaining = fuel_tank - fuel_consumed
    Endurance = fuel_remaining / fuel_used
  


   
    print("\nFuel Consumed: ",fuel_consumed," liters")
    print("==========================================")
    print("\nFuel remaining: ",fuel_remaining," liters")
    print("==========================================")
    print("\nRunning Time remaining: ",Endurance," minutes")
    print("==========================================")

    again = input("\nAnother input (y/n)")
    if again == "n":
        break
