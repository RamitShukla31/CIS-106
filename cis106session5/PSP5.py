#Last Name: Ramit Shukla  Date created: 2/16/2026

EmployeelastName = input("Enter Employee last Name: ")
EmployeeSalary = input("Enter Employee Salary: ")
EmployeeJobLevel = int(input("Enter Employee Job Level: "))

EmployeeSalary = float(EmployeeSalary)

if EmployeeJobLevel>=10:
    BonusRate = 25
elif EmployeeJobLevel>=5 and EmployeeJobLevel<=9:
    BonusRate = 20
else:
    BonusRate = 10

EmployeeBonus = EmployeeSalary*(BonusRate/100)

print(f"Employee last Name: {EmployeelastName}")
print(f"Employee Bonus: {EmployeeBonus}")

    

