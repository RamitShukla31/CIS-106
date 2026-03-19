#Last Name: Ramit Shukla  Date created: 3/15/2026

def CompExtPrice(qty, unitprice):
    extprice = qty * unitprice

    if extprice > 10000.00:
        discamt = extprice * 0.10
    else:
        discamt = 0.0
    
    finalprice = extprice - discamt
    return finalprice


totalextPrice = 0.0

r = input("Do you want to compute extended price (y/n)? ").lower()

while r == "y":
    qty = float(input("Enter quantity: "))
    unitprice = float(input("Enter unit price: "))
    
    extprice = CompExtPrice(qty, unitprice)

    totalextPrice = totalextPrice + extprice

    print(f"Extended price after discount is ${extprice}")

    r = input("Do you want to compute extended price (y/n)? ").lower()


print(f"Total of all extended prices: ${totalextPrice}")



