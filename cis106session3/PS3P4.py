#Name:Ramit Shukla, Date created:1/31/2026

Automake = input("Enter Auto make: ") 
Automodel = input("Enter Auto model: ") 
MsrpAmount = input("Enter Msrpamount: ")
Discountpercent = input("Enter Discount percent: ")

MsrpAmount = float(MsrpAmount)
Discountpercent = float(Discountpercent)

AmountOff = MsrpAmount * Discountpercent
DiscountedPrice = MsrpAmount - AmountOff

print("\nAuto Make:", Automake)
print("Auto Model:", Automodel)
print("MSRP Amount:", MsrpAmount)
print("Discount Percent:", Discountpercent)
print("Amount Off:", AmountOff)
print("Discounted Price:", DiscountedPrice)









