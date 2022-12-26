###########################################################################################
# Scipt: House Energy Budget 2022                                                         #
# By JF                                                                                   #
# All values are in €                                                                     #
# Purpose: Input the different fuel (energy) costs, sum the costs applie the discAount    #
# Output the cost of each fuel (energy input) to the screen                               #
# Sum all costs, givening a total cost                                                    #
# apply the discount                                                                      #
# Output the difference between the budget and the total energy cost - discount           #
# Values may be changes as input costs change                                             #
#                                                                                         #
# Tested: on Python v3.10.5 on windows 10                                                 #
#                                                                                         #
# Revision History:                                                                       #
# Version: A01  01-oct-22                                                                 #
# This script has no error handling, by design.                                           #          
###########################################################################################


energy_budget = 5500  #variable called energy_budget equal to a static value

# Electricity bill (6 bills per year)
electricity = 200 * 2 + 241* 3 + 401*4 + 477*2 #variable called electricity equal to a static values and Arithmetic operators, multiplications and addition

# Propane Cylinder 47kg 
gas = 149 * 1 #variable called gas equal to a static value and Arithmetic operators, multiplications only

# kerosene cost per ltr
kerosene = 900 * 1.24  #variable called kerosene equal to a static value and Arithmetic operators, multiplications only

# Bags of Coal 
coal = 26 * 30  #variable called coal equal to a static value and Arithmetic operators, multiplications only

# Bale of Briquettes
bob = 20 * 6.50  #variable called bob equal to a static value and Arithmetic operators, multiplications only

# Sundries
sundries = 220 #variable called sundries equal to a static value

gross_cost = electricity + gas + kerosene + coal + bob + sundries #variable called gross_cost is equal to the sum of of previous variables
discount = gross_cost * .1 #variable called discount equal to variable called gross_cost multiplied by .1 (10%) 
net_cost = gross_cost - discount #variable called net_cost is equal to variable called gross_cost substract variable call discount
remaider_in_budget = energy_budget - net_cost #variable called remaider_in_budget is equal to variable called energy_budget subtract variable called net_cost

#Function print, print data to a screen, out-put to a Dos prompt
print("\nElectricity Cost: €",electricity) # print function, print variable electricity
print("Propane Gas Cost: €",gas) # print function, print variable gas
print("Home Heating Oil: €",kerosene) # print function, print variable kerosene
print("Coal for the year: €",coal) # print function, print variable coal
print("Briquettes for the year: €",bob) # print function, print variable bob (Bale of Briquettes)
print("Sundries for the year: €",sundries)  # print function, print variable sundries

#Function print, print data to a screen, out-put to a Dos prompt
print("\nGross Energy Cost For The Year: €",gross_cost) # print function, print variable gross_cost
print("Discount is 10% : €",discount) # print function, print variable discount
print("Net Enegy Cost For The Year: €",net_cost) # print function, print net_cost
print("\nRemainder in the Budget For The Year: €",remaider_in_budget) # print function, print variable remaider_in_budget


