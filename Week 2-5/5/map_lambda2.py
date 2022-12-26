#circumference = lambda radius : 2 * 3.142 * radius
# area = lambda radius : 3.142 * radius * radius
radius = 5
height = 9
length = 4


Volume_cyl = lambda radius : 3.142 * radius * radius * height
volume_cone = lambda radius : 3.142 * radius * radius * height/3


Area_rectangle = lambda length : length * height
Perimeter_rectangle = lambda length : (length + height) * 2 

print(Volume_cyl(radius), volume_cone(radius))
print(Area_rectangle(length), Perimeter_rectangle(length))