
# function def find_num                                                                       #
# number_list is a list of numbers, number is a integer                                       #
# ->boolean built-in data types. It's used to represent the truth or false of an expression   #
def find_num(number_list: list, number: int)->boolean:
# Look in number list from my number #
 for iterate_number in number_list:
 # if my number is found return a true value to the screen #
 if iterate_number == number:
 return True
 #conditional statements (if statements), and decides what to do if the condition is False #
 else:
 pass
 # my list of numbers 
result = find_num([1,2,3,4,5,6,7,8], 9)
# function print result to a screen
print(result)




 #if iterate_number == number:
 #return True
 #else
 #if iterate_number != number:
 #return False