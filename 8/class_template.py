"""
Joseph Forde
Exercise_8
Student number: L00169708
Template
"""

class Template(object):

    def __init__(self):
        self.value_1 = "11"
        self.value_2 = "22"
        self.value_3 = "33"
        current_class = self.__class__
        inits = []
        while (current_class.__name__ != "Template"):
            inits.append(current_class.init)
            current_class = current_class.__bases__[0]
        for i in reversed(inits):
            i(self)

    def init(self):
        pass

    def info(self):
        print(self.value_1)
        print(self.value_2)
        print(self.value_3)
       # print ""

class Test(Template):
    def init(self):
        self.value_1 = "88"
        self.value_2 = "99"

class Carron(Test):
    def init(self):
        self.value_1 = "USS kelvin"
        self.value_3 = "USS Yamato"

class Tarmon(Carron):
    def init(self):
        self.value_2= "USS Stargazer"

#Temp_1 = Test()
Temp_2 = Carron()
Temp_3 = Tarmon()
#Temp_1.info()
Temp_2.info()
Temp_3.info()