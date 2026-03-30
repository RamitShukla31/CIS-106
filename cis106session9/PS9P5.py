#Last Name: Ramit Shukla  Date created: 3/29/2026

def CompAssessedValue(countyvalue, marketvalue):
    if countyvalue == "Cook":
        assesspercent = 0.90
    elif countyvalue == "DuPage":
        assesspercent = 0.80
    elif countyvalue == "McHenry":
        assesspercent = 0.75
    elif countyvalue == "Kane":
        assesspercent = 0.60
    else:
        assesspercent = 0.70

    assessedvalue = marketvalue * assesspercent
    return assessedvalue


totalmarketvalue = 0.0
totalassessedvalue = 0.0

userresponse = input("Do you want to do this program (Yes or No): ")

while userresponse.lower() == "yes":
    countyvalue = input("Enter county: ")
    marketvalue = float(input("Enter market value of home: "))

    assessedvalue = CompAssessedValue(countyvalue, marketvalue)

    print(f"County: {countyvalue}")
    print(f"Assessed Value: ${assessedvalue}")

    totalmarketvalue = totalmarketvalue + marketvalue
    totalassessedvalue = totalassessedvalue + assessedvalue

    userresponse = input("Do you want to continue with this program? ")

print(f"Total Market Value: ${totalmarketvalue}")
print(f"Total Assessed Value: ${totalassessedvalue}")