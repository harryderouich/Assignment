#Harry Derouich
#12/09/14
#Garden Calculation exercise

print("Hello User!")
length = int(input("Please enter the length of your garden in metres: "))
width = int(input("Please enter the width of your garden in metres: "))

new_length = length - 2
new_width = width - 2

total_area = new_length * new_width

total_cost = total_area * 10
print("The total cost will be £{0}".format(total_cost))
