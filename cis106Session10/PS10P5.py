#Last Name: Ramit Shukla  Date created: 4/6/2026

def CompTotalTax(quantityvalue, unitpricevalue):
    global totalvalue, taxvalue

    totalvalue = quantityvalue * unitpricevalue
    taxvalue = totalvalue * 0.07


quantityvalue = float(input("Enter quantity: "))
unitpricevalue = float(input("Enter unit price: "))

CompTotalTax(quantityvalue, unitpricevalue)

print(f"Total: ${totalvalue}")
print(f"Tax: ${taxvalue}")