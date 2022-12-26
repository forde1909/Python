"""
Joseph Forde
Exercise_10
mytime
Student number: L00169708
"""
"""" 
OS utilities, forked from the Comm module of SD-Node, written c. 2017 
Tested with Python >=3.6 
By: JOR 
v0.1 26AUG21 
""" 
def cpu_load(): 
    # Return significant numbers relating to the CPU 
    print(f"Number of CPUs: {psutil.cpu_count()}" ) 
    print(f"CPU load: {psutil.cpu_percent()}") 
    return(psutil.cpu_count(), psutil.cpu_percent())
