#Harry Derouich
#23/09/14
#Assignment Statment Spot Check - Question 1

import math

print("Hello user")
pool_width = int(input("Please enter the width of your swimming pool: "))
pool_length = int(input("Please enter the length of your swimming pool: "))
pool_depth = int(input("Please enter the depth of your swimming pool: "))


main_section_volume = pool_length * pool_width * pool_depth

radius = pool_width / 2
circle_area = math.pi * (radius**2)

half_circle_volume = (circle_area / 2) * pool_depth

total_volume = main_section_volume + half_circle_volume

rounded_volume = round(total_volume, 2)

print("The total volume of the pool is: {0}!".format(rounded_volume))
