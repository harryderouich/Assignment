#Harry Derouich
#19/09/14
#Currency Conversion exercise

print("Hello User!")

whole_number = int(input("Please enter the total number: £"))

twenty_notes = whole_number // 20
twenty_remain = whole_number % 20

ten_notes = twenty_remain // 10
ten_remain = twenty_remain % 10

five_notes = ten_remain // 5
five_remain = ten_remain % 5

two_coin = five_remain // 2
two_remain = five_remain % 2

one_coin = two_remain // 1

print("This goes into {0} £20 notes, {1} £10 notes, {2} £5 notes, {3} £2 coins, and {4} £1 coins.".format(twenty_notes, ten_notes, five_notes, two_coin, one_coin))



