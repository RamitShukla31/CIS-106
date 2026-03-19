#Last Name: Ramit Shukla  Date created: 3/18/2026

def CompPayRate(jobcodevalue):
    if jobcodevalue == "L":
        payratevalue = 25.0
    elif jobcodevalue == "A":
        payratevalue = 30.0
    elif jobcodevalue == "J":
        payratevalue = 50.0
    else:
        payratevalue = 0.0
    return payratevalue


totalgrosspay = 0.0
employeecount = 0

userresponse = input("Do you want to do this program (Yes or No): ")

while userresponse.lower() == "yes":
    employeelastname = input("Enter employee last name: ")
    jobcodevalue = input("Enter job code (L, A, J): ").upper()
    hoursworked = float(input("Enter hours worked: "))

    payratevalue = CompPayRate(jobcodevalue)

    if hoursworked > 40:
        overtimehours = hoursworked - 40
        regularpay = 40 * payratevalue
        overtimepay = overtimehours * payratevalue * 1.5
        grosspayvalue = regularpay + overtimepay
    else:
        grosspayvalue = hoursworked * payratevalue

    print(f"Employee Last Name: {employeelastname}")
    print(f"Gross Pay: ${grosspayvalue}")

    totalgrosspay = totalgrosspay + grosspayvalue
    employeecount = employeecount + 1

    userresponse = input("Do you want to continue with this program? ")

print(f"Total Gross Pay: ${totalgrosspay}")
print(f"Total Employees Entered: {employeecount}")
