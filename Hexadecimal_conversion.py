#Harry Derouich
#18/09/14
#Hexadecimal converison task

denary_value = int(input("Please enter a denary number"))
print(denary_value)
binary_value = ""

while denary_value > 0:
    binary_value = str(denary_value % 2) + binary_value
    denary_value = denary_value / 2

print("The binary equivalent is {0}".format(binary_value))
