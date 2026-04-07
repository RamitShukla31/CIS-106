#Last Name: Ramit Shukla  Date created: 4/5/2026

def CompDiscount(quantityvalue, pricevalue, discountrate):
    totalprice = quantityvalue * pricevalue
    discountamount = totalprice * discountrate
    discountedprice = totalprice - discountamount
    return discountamount, discountedprice


quantityvalue = float(input("Enter quantity: "))
pricevalue = float(input("Enter price: "))
discountrate = float(input("Enter discount rate (e.g., 0.10 for 10%): "))

discountamount, discountedprice = CompDiscount(quantityvalue, pricevalue, discountrate)

print(f"Quantity: {quantityvalue}")
print(f"Price: ${pricevalue:.2f}")
print(f"Discount Amount: ${discountamount:.2f}")
print(f"Discounted Price: ${discountedprice:.2f}")

