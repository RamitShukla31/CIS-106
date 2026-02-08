#Name: Ramit Shukla Date created: 2/7/2026

ItemName = input("Enter Item Name: ") 
ItemQuantity = input("Enter Item Quantity: ") 

ItemQuantity = int(ItemQuantity)

if ItemName == "A": 
    UnitPrice = 10.00
else:
    UnitPrice = 20.00

ExtendedPrice = ItemQuantity * UnitPrice

print(f"Item Name = {ItemName}") 
print(f"Unit Price = {UnitPrice}") 
print(f"Extended Price = {ExtendedPrice}") 



