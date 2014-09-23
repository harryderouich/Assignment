#Harry Derouich
#23/09/14
#Assignment Statment Spot Check - Question 2

print("Hello user")

total_weight = int(input("Please enter the total weight: "))

no_100 = total_weight // 100
rem_100 = total_weight % 100

no_50 = rem_100 // 50
rem_50 = rem_100 % 50

no_10 = rem_50 // 10
rem_10 = rem_50 % 10

no_5 = rem_10 // 5
rem_5 = rem_10 % 5

no_2 = rem_5 // 2
rem_2 = rem_5 %2

no_1 = rem_2 // 1

print("The weights needed to balance are: {0}x100g weights, {1}x50g weights, {2}x10g weights, {3}x5g weights, {4}x2g weights and {5}x1g weights!".format(no_100, no_50, no_10, no_5, no_2, no_1))
