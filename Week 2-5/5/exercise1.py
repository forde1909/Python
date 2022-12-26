

# function def divisible                                                                               #
# numerator has a integer value, denominator has a integer value                                       #
# ->boolean built-in data types. It's used to represent the truth or false of an expression            #
def divisible(numerator: int, denominator: int)->boolean:
 # return is a special statement that you can use inside a function to send the function's result back #
 # % Modulo Operator, numerator & denominator are integer values, == 0 equal to 0 (zero) at the start  #
 return numerator % denominator == 0
# Function print data to the screen, Dos prompt, divisible 30 can be divisible by 4                    # 
print(divisible(30,4))


# The Function will return True
# Why, 30 is divisible by 4