#Harry Derouich
#16/09/14
#Swimming pool volume calculator

print("Hello user")
#All the data needed is inputted
width_metres = int(input("Please enter the width of your swimming pool in metres: "))
length_metres = int(input("Please enter the length of your swimming pool in metres: "))
depth_shallow = int(input("Please enter the shallow depth of your swimming pool in metres: "))
depth_deep =int(input("Please enter the deepest depth of your swimming pool in metres: "))

extra_length = depth_deep - depth_shallow

cross_rectangle = length_metres * depth_shallow
cross_triangle = (length_metres * extra_length) / 2

cross_area = cross_triangle + cross_rectangle

volume_total = cross_area * width_metres

print("The total amount of water needed to fill the pool is {0}m³".format(volume_total))





