"""
Joseph Forde
Exercise_8
Student number: L00169708
"""

# Create a class
class myclass1(object):
  def __init__(self, name, age, year,):
    self.name = name
    self.age = age
    self.year = year


class myclass2(object):
  def __init__(self, student, employed, income,):
    self.student = student
    self.employed = employed
    self.income = income


# New Class from the two parent classes
class myclass3(myclass1, myclass2):         
   def __init__(self, name, age, year, student, employed, income,):  
      myclass1.__init__(self, name, age, year,) 
      myclass2.__init__(self, student, employed, income,)

PT = myclass3("\nMichael", "\n19 years old", "\nBorn the year of the Rat", "\nstudent", "\nemployed", "\nincome = $50,000",)
p1 = myclass1("\nMichael", "19 years old", "Born the year of the Rat",)
p2 = myclass1("\nKim ly", "14 years old", "Born the year of the Golden Pig",)
p3 = myclass1("\nThi Anh", "12 years old", "Born the year of the Tiger",)
p4 = myclass1("\nLuke.", "7 years old", "Born the year of the Cat",)

print (PT.name, PT.employed, PT.income)

print(p4.name)
print(p4.age)
print(p4.year)

print(p3.name)
print(p3.age)
print(p3.year)

print(p2.name)
print(p2.age)
print(p2.year)

print(p1.name)
print(p1.age)
print(p1.year)