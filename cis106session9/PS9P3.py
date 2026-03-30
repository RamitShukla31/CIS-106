#Last Name: Ramit Shukla  Date created: 3/29/2026

def CompOutTheDoor(msrpvalue, makevalue, modelvalue, electriccode):
    if electriccode == "Y":
        discountpercent = 0.30
    elif makevalue == "Honda" and modelvalue == "Accord":
        discountpercent = 0.10
    elif makevalue == "Toyota" and modelvalue == "Rav4":
        discountpercent = 0.15
    else:
        discountpercent = 0.05

    discountamount = msrpvalue * discountpercent
    newmsrpvalue = msrpvalue - discountamount
    salestaxvalue = newmsrpvalue * 0.07
    finalprice = newmsrpvalue + salestaxvalue

    return finalprice


totalmsrpvalue = 0.0
totalsalesvalue = 0.0

userresponse = input("Do you want to do this program (Yes or No): ")

while userresponse.lower() == "yes":
    makevalue = input("Enter make (Honda/Toyota/etc): ")
    modelvalue = input("Enter model: ")
    electriccode = input("Is it electric? (Y or N): ").upper()
    msrpvalue = float(input("Enter MSRP: "))

    finalprice = CompOutTheDoor(msrpvalue, makevalue, modelvalue, electriccode)

    print(f"Make: {makevalue}")
    print(f"Model: {modelvalue}")
    print(f"Final Price: ${finalprice}")

    totalmsrpvalue = totalmsrpvalue + msrpvalue
    totalsalesvalue = totalsalesvalue + finalprice

    userresponse = input("Do you want to continue with this program? ")

print(f"Total MSRP: ${totalmsrpvalue}")
print(f"Total Sales Price: ${totalsalesvalue}")