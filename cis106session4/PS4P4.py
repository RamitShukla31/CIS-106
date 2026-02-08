#Name: Ramit Shukla Date created: 2/7/2026

NameofAppliance = input("Enter Name of Appliance: ") 
CostofAppliance = input("Enter cost of Appliance: ") 


CostofAppliance = float(CostofAppliance) 

if CostofAppliance > 1000:
    WarrantyCost = CostofAppliance * (10/100)
else: 
    WarrantyCost = CostofAppliance * (5/100)

WarrantyCost = round(WarrantyCost, 2) 

TotalCost = CostofAppliance + WarrantyCost

print(f"Name of Appliance = {NameofAppliance}")
print(f"Cost of Appliance = {CostofAppliance}")
print(f"Cost of Warrant = {WarrantyCost}") 
print(f"Cost of Total = {TotalCost}") 

