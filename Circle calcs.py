#Harry Derouich
#19/09/14
#Circumference calculation exercise

import math

print("Hello user")
radius = int(input("Please enter the radius of the circle in centimetres: "))

circum = 2 * math.pi * radius
area = math.pi * radius**2

circum_round = round(circum, 2)
area_round = round(area, 2)

print("The circumference is {0}cm, and the area is {1}cm squared".format(circum_round, area_round))
