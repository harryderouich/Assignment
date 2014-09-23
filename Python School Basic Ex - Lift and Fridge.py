#Harry Derouich
#23/09/14
#Python School - Basic Exercises: Question 1

print("Hello user")

lift_height = float(input("Please enter the height of the lift: "))
lift_width = float(input("Please enter the width of the lift: "))
lift_depth = float(input("Please enter the depth of the lift: "))

fridge_height = float(input("Please enter the height of the fridge: "))
fridge_width = float(input("Please enter the width of the fridge: "))
fridge_depth = float(input("Please enter the depth of the fridge: "))

volume_lift = lift_height * lift_width * lift_depth
volume_fridge = fridge_height * fridge_width * fridge_depth

volume_left = volume_lift - volume_fridge

print("The total volume left is: {0}".format(volume_left))

