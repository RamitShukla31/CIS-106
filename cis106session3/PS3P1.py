#Name:Ramit Shukla,  Date Created:1/29/2026

Stocksymbol = input("Enter the stock symbol: ")
Numberofshares = input("Enter the number of shares: ")
Costpershare = input("Enter the cost per share: ")

Amountinvested = float(Numberofshares)*float(Costpershare)

print(f"For stock symbol {Stocksymbol}, Amount invested = {Amountinvested}")