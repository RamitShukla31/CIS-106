#Name: Ramit Shukla,  Date created: 2/7/2026

ItemQuantity = input("Enter Item Quantity: ")

ItemQuantity = int(ItemQuantity)

if ItemQuantity >= 1000: 
    UnitPrice = 3.00
else:
    UnitPrice = 5.00

ExtendedPrice = ItemQuantity * UnitPrice
ApplicableTax = ExtendedPrice * (7/100)
ApplicableTax = round(ApplicableTax, 2)
TotalPrice = ExtendedPrice + ApplicableTax

print(f"Item Quantity = {ItemQuantity}")
print(f"Unit Price = {UnitPrice}")
print(f"Extended Price = {ExtendedPrice}") 
print(f"Applicable Tax = {ApplicableTax}") 
print(f"Total Price = {TotalPrice}") 



