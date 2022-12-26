# Python program to print Even Numbers in a List

# list of Fibonacci Sequence numbers
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181.]

 
# iterating each number in list
for num in list1:
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")

  # return True

if num % 2 != 0:
  print("\nTrue!")
else:
  print("\nFalse!")