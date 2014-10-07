#test grading program

testScore = int(input("Please enter your test score: "))
if 0 < testScore <= 40:
    print("E grade")

elif 40 < testScore <= 50:
    print("D grade")
    

elif 50 < testScore <= 60:
    print("C grade")

elif testScore <= 70:
    print("B grade")

elif testScore <= 80:
    print("A grade")

else: print("Fail") 
