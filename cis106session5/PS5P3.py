#Last Name: Ramit Shukla  Date created: 2/15/2026

PrincipalAmount = int(input("PrincipalAmount: "))
YearstoMaturity = int(input("Enter years of Maturity: "))

if PrincipalAmount>100000 and YearstoMaturity == 5:
    InterestRate = 6
elif 50000 <= PrincipalAmount <= 100000 and YearstoMaturity == 10:
    InterestRate = 5
elif  50000 <= PrincipalAmount <= 100000 and YearstoMaturity == 5:
    InterestRate = 4
else:
    InterestRate = 2

    firstyearInterest = PrincipalAmount * (InterestRate/100)

print(f"PrincipalAmount = {PrincipalAmount}") 
print(f"Interest Rate = {InterestRate}") 
print(f"First year Interest = {firstyearInterest}")



