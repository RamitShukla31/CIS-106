#Name: Ramit Shukla Date created: 2/7/2026

NumberofBooks = input("Enter Number of Books: ") 
CostPerBook = input("Enter Cost per Book: ") 

NumberofBooks = int(NumberofBooks)
CostPerBook = int(CostPerBook) 


OrderTotal = NumberofBooks*CostPerBook 

if OrderTotal>50.00: 
    ShippingCharge=0
if OrderTotal<=50.00:
    ShippingCharge=25.00

OrderTotalWithShippingCharge = OrderTotal + ShippingCharge

if ShippingCharge == 0:
    ShippingText = "Free"
else:
    ShippingText = ShippingCharge


print(f"Order total with shipping charge = {OrderTotalWithShippingCharge}") 
print(f"Shipping Charge = {ShippingText}") 

