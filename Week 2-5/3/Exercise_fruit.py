

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("List of fruite",fruits)

apple = fruits.count('apple')
print("\nNumber of apples is :",apple) # print function, print variable

tangerine = fruits.count('tangerine')
# print(tangerine)
print("\nNumber of tangerine is :",tangerine) # print function, print variable

banana_1 = fruits.index('banana')
print("\nIndex location of first banana is :",banana_1) # print function, print variable

banana_2 = fruits.index('banana', 4)  # Find next banana starting a position 4
print("\nIndex location of the next banana is :",banana_2) # print function, print variable

# Reversing a list	
# Syntax: reversed_list = systems[start:stop:step] 
reversed_list = fruits[::-1]
# updated list
print("\nList in reverse:", reversed_list)

fruits.append('grape')
print("\nNew list with grape added",fruits)

fruits.sort()
print("\nList is ordered alphabetically",sorted(fruits))

# removes random item of set fruits
print("\nPop() removes:", fruits.pop())


