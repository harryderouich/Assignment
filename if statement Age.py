#Harry Derouich

age = int(input("Please enter your age: "))
if age >=18:
    print("You can vote!")

else:
    print("Sorry you can't vote yet")

years_retire = 65-age
print("Also it is only {0} years until you retire!".format(years_retire))

