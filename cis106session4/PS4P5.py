#Last Name: Ramit Shukla  Date created: 2/7/2026

UserLastName = input("Enter User Last Name: ") 
NumberofDependents = input("Enter Number of dependents: ") 
GrossIncome = input("Enter Gross Income: ") 

NumberofDependents = int(NumberofDependents)
GrossIncome = float(GrossIncome) 

AdjustedGrossIncome = GrossIncome-NumberofDependents*12000

if AdjustedGrossIncome > 50000:
    TaxRate = 20
else:
    TaxRate = 10

IncomeTax = AdjustedGrossIncome * (TaxRate/100)

IncomeTax = round(IncomeTax, 2) 

if IncomeTax < 0: 
    IncomeTax = 100

print(f"User Last Name = {UserLastName}")
print(f"Gross Income = {GrossIncome}") 
print(f"Number of Dependants = {NumberofDependents}")
print(f"Adjusted Gross Income = {AdjustedGrossIncome}")
print(f"Enter Income Tax = {IncomeTax}")





