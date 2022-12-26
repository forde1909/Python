energy_budget = 5500

# Electricity bill (6 bills per year)
electricity = 200 * 2 + 241* 3 + 401*4 + 477*2

# Propane Cylinder 47kg 
gas = 149 * 1

# kerosene cost per ltr
kerosene = 900 * 1.24

# Bags of Coal 
coal = 26 * 30

# Bale of Briquettes
bob = 20 * 6.50

# Sundries
sundries = 220

gross_cost = electricity + gas + kerosene + coal + bob + sundries
discount = gross_cost * .1
net_cost = gross_cost - discount
remaider_in_budget = energy_budget - net_cost 

print("\nElectricity Cost: €",electricity)
print("Propane Gas Cost: €",gas)
print("Home Heating Oil: €",kerosene)
print("Coal for the year: €",coal)
print("Briquettes for the year: €",bob) 
print("Sundries for the year: €",sundries)  

print("\nGross Energy Cost For The Year: €",gross_cost)
print("Discount is 10% : €",discount) 
print("Net Enegy Cost For The Year: €",net_cost) 
print("\nRemainder in the Budget For The Year: €",remaider_in_budget) 


