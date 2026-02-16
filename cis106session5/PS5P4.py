#Last Name: Ramit Shukla  Date created: 2/15/2026

numberofConcertTickets = int(input("Enter Number of Concert Tickets: ")) 

if numberofConcertTickets>=25:
    PriceperTicket = 50
elif numberofConcertTickets>=10:
    PriceperTicket = 60
elif numberofConcertTickets>=5:
    PriceperTicket = 70
else:
    PriceperTicket = 75
        
TotalCost = numberofConcertTickets*PriceperTicket

print(f"Number of concert tickets:  {numberofConcertTickets}")
print(f"Price per Ticket: {PriceperTicket}")
print(f"Total Cost: {TotalCost}")







