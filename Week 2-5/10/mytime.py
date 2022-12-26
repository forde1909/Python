"""
Joseph Forde
Exercise_10
mytime
Student number: L00169708
"""

from datetime import datetime as dt 
# Get the current time, returns a value like 2022-10-09 17:46:45.151666 
today = dt.now() 
#print(today) 
# Get the current Year, returns a value like 2022 
Year = dt.now().strftime("%Y")
#print(Year) 
# Get the current Month of the Year, returns a value like October 
Month = dt.now().strftime("%B")
#print(Month)
# Get the current day of the week, returns a value like Friday 
Day = dt.now().strftime("%A")
#print(Day)
# Get the current time 12-Hour:Minute:Second:AM
Time = dt.now().strftime("\nCurrent GMT is: %I:%M:%S %p")
print(Time) # 12-Hour:Minute:Second:AM
# Get the current Yeay,Month,Day, returns a value like 2022,October,Friday 
Date = dt.now().strftime("To Currnt Year, Month, Day of week is: %Y, %B, %A\n" )
print(Date)
print()
