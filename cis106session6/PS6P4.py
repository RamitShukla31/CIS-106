#Last Name: Ramit Shukla  Date created: 2/22/2026

userResponse = input("Do you want to run this program: ")

TotalGrossPay = 0
EmployeeCount = 0

while userResponse == "Yes":
    EmployeeLastName = input("Enter Employee Last Name: ")
    HoursWorked = int(input("Enter Hours Worked: "))
    PayRate = float(input("Enter Pay Rate: "))

    if HoursWorked > 40:
        RegularPay = 40*PayRate
        OvertimeHours = HoursWorked - 40
        Overtimepay = OvertimeHours*(PayRate*1.5)
        GrossPay = RegularPay + Overtimepay
    else:
        GrossPay = HoursWorked*PayRate

    print(f"Employee Last Name: {EmployeeLastName}")
    print(f"Employee Gross Pay: {GrossPay}")
   
    TotalGrossPay = TotalGrossPay + GrossPay
    EmployeeCount = EmployeeCount + 1

    userResponse = input("Do you want to run this loop again? ")

if EmployeeCount > 0:
    AveragePay = TotalGrossPay/EmployeeCount
else:
    AveragePay = 0

print(f"Total Enployee Count: {EmployeeCount}")
print(f"Average Employee Pay: {AveragePay}")        
    




        

