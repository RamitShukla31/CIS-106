#Last Name: Ramit Shukla  Date created: 2/22/2026

UserResponse = input("Do you want to run this program: ")

TotalDiscount = 0

while UserResponse == "Yes":
    Quantity = int(input("Enter Qunatity: "))
    ItemPrice = float(input("Enter Item Price: "))

    extendedPrice = Quantity*ItemPrice

    if extendedPrice>10000.00:
        discountPercent = 0.25
    else:
        discountPercent = 0.10

    DiscountAmount = extendedPrice*discountPercent
    TotalPrice = extendedPrice - DiscountAmount

    print(f"Extended Price: {extendedPrice}")
    print(f"Discount Amount: {DiscountAmount}")
    print(f"Total Price: {TotalPrice}")

    TotalDiscount = TotalDiscount + DiscountAmount

    UserResponse = input("Do you want to run this loop again? ")

print(f"Sum of all discounts {TotalDiscount}")
 






