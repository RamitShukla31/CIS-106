ItemPrice = input("Enter item price: ")
Percentdiscount = input("Percent discount: ")

Discountamount = float(ItemPrice) * (float(Percentdiscount)/100)
Discountedprice = float(ItemPrice)-Discountamount

print(f"For item price {ItemPrice}, discount amount is {Discountamount}")
print(f"Disocunted price = {Discountedprice} ")