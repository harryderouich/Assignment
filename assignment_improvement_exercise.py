#john bain
#variable improvement exercise
#05-09-12

import math

radius = int(input("please enter the radius of the circle: "))

circum = 2* math.pi * radius
circum = round(circum,2)

area = math.pi * radius**2
area = round(area,2)

print("The circumference of this circle is {0}.".format(circum))
print("The area of this circle is {0}.".format(area))
