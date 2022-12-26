"""
Joseph Forde
Exercise_8
Student number: L00169708
Template
"""
#In any complex application, create a base class which will never be instantiated. 
class Device(): 
    # Define a class object attribute, it will be the same for any instance of the class 
    pi = 3.142 
    
    # Constructor, called whenever an instance of the class is created. 
    def __init__(self) -> None: 
        print("Running constructor for base class") 
        # Create attributes and set initial values 
        self.debug = False 
        
    def run(self): 
        raise NotImplementedError("This is an abstract class, do not instantiate") 
    
    def calculate_crc(self, frame:str)->int: 
        print("Checking CRC from base") 
        # Put real code in here, this is a dummy value for initial setup 
        crc = 123456789 
        return crc