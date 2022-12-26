"""
Joseph Forde
Exercise_7
Student number: L00169708
"""


while True:
    try:
        # Fuel in the tank
        fuel_tank = input("\nEnter Volume of fuel in Liters in tank:   ")
        fuel_tank = float(fuel_tank)
        if fuel_tank != 0:
           pass    # pass here

        time_ = input ("\nTime running in minutes:   ")
        time_ = float(time_)
        if time_ != 0:
            pass    # pass here

    except ValueError:
        print("No valid input! Please try again ...")
       

    # Fuel Consumption in Liters/Per minute
    fuel_used = float(0.03)

    #Get distance driven from the user
    #time_ = input ("\nTime running in minutes:   ")
    #time_ = int(time_)
    #time_ = float(time_)
    #if time_ != 0:
     #   pass # pass here

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
