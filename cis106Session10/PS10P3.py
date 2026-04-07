#Last Name: Ramit Shukla  Date created: 4/6/2026

def CompSalesStats(salesvalue):
    if salesvalue > 100000:
        commissionvalue = salesvalue * 0.10
    else:
        commissionvalue = salesvalue * 0.05

    targetvalue = salesvalue * 0.05
    return commissionvalue, targetvalue


saleslastname = input("Enter salesperson last name: ")
salesvalue = float(input("Enter sales amount: "))

commissionvalue, targetvalue = CompSalesStats(salesvalue)

print(f"Salesperson Last Name: {saleslastname}")
print(f"Commission: ${commissionvalue}")
print(f"Next Year Target: ${targetvalue}")

