#Volume of a Cylinder                        #
#Volume = 3.12 * Radius * Radius * Height    #
#Volume of a Cone                            #
#Volume = 3.12 * Radius * Radius * Height/3  #
#Area of a Rectangle                         #
#Area = Length * Height                      #
#Perimeter of a Rectangle                    #
#Perimeter = (Length + height) *2            # 
##############################################

radius = 5
height = 9
length = 4


Volume_cyl = lambda radius : 3.142 * radius * radius * height
volume_cone = lambda radius : 3.142 * radius * radius * height/3


Area_rectangle = lambda length : length * height
Perimeter_rectangle = lambda length : (length + height) * 2 

print(Volume_cyl(radius), volume_cone(radius))
print(Area_rectangle(length), Perimeter_rectangle(length))