#Last Name: Ramit Shukla  Date created: 2/15/2026

PartNo = input("Enter part Number: ") 
Quantity = int(input("Enter Quantity: "))

if PartNo == "10" or PartNo == "55": 
    UnitCost = 1.00
elif PartNo == "99":
    UnitCost = 2.00
elif PartNo == "80" or PartNo == "70":
    UnitCost = 3.00
else:
    UnitCost = 5.00 

TotalCost = Quantity*UnitCost 

print(f"Part Number: {PartNo}") 
print(f"Unit Cost: {UnitCost}") 
print(f"Total Cost:{TotalCost}")
