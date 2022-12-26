
"""
File utilities, forked from the Comm module of SD-Node, written c. 2017 
Tested with Python >=3.6 

Joseph Forde
Exercise_10
Student number: L00169708
 
By: JOR 
v0.1 26AUG21 
""" 

from file_utilities import path_name, log_file_name 
from os_utilities import detect_os 

# Check the OS in use, and figure out a log file name and path 
this_os = detect_os()
log_path = path_name() 
filename = log_file_name(".log") 
print(log_path + filename )