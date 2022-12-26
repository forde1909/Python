def validate_integer(): 
    # Loop forever
    while True: 
     try: 
        user_input = int(input("Enter an integer value: ")) 
     except: 
        #Bad value, 
        print("Error") 
        continue 
     else: 
        print("Valid input") 
        # Good value, exit the loop 
        break 
     finally: 
        # Only runs after the except, continue 
        print("Try again - enter an integer value only!") 


validate_integer()