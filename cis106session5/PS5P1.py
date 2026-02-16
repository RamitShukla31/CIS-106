#Last Name: Ramit Shukla  Date created: 2/15/2026

QuantityofWidgets = int(input("Enter Quantity of Widgets: "))

if QuantityofWidgets>10000:
    WidgetPrice=10
elif QuantityofWidgets>=5000:
    WidgetPrice = 20
else:
    WidgetPrice = 30

ExtendedPrice = QuantityofWidgets*WidgetPrice

Taxamount = ExtendedPrice*(7/100) 

TotalPrice = ExtendedPrice+Taxamount

print(f"Extended Price = {ExtendedPrice}")
print(f"Tax amount = {Taxamount}") 
print(f"Total price = {TotalPrice}") 





