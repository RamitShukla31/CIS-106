#Last Name: Ramit Shukla  Date created: 3/6/2026
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(script_dir, "data3.txt"), "r")

# get first data line
lastName = f.readline().strip()

totalBonus = 0

while lastName != "":
    salary = float(f.readline())

    if salary >= 100000.00:
        bonusPercentage = 20/100
    elif salary >= 50000.00:
        bonusPercentage = 15/100
    else:
        bonusPercentage = 10/100

    empBonus = salary * bonusPercentage

    totalBonus = totalBonus + empBonus

    # display data
    print("Employee Last Name:", lastName)
    print("Salary:", salary)
    print("Bonus:", empBonus)

    # get next data
    lastName = f.readline().strip()

print("Total bonus:", totalBonus)

f.close()

