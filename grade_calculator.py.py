average = float(input("Enter your average: "))

"""If 100 ≥ average ≥ 90, this mean thee grade is Excellent
b. If 90 > average ≥ 80, this mean thee grade is Very Good
c. If 80 > average ≥ 70, this mean thee grade is Good
d. If 70 > average ≥ 50, this mean thee grade is Passed
e. If 50 > average ≥ 0, this mean thee grade is Failed
otherwise : erorr
"""
if average >= 90 and average < 100:
    print("Exellent")
elif average >= 80 and average < 90:
    print("Very Good")
elif average >= 70 and average < 80:
    print("Good")
elif average >= 50 and average < 70:
    print("Passed")
elif average >= 0 and average < 50:
    print("Failed")
else:
    print("erorr")
