#Last Name: Ramit Shukla  Date created: 3/29/2026

def CompTicketPrice(milesvalue):
    if milesvalue >= 30:
        ticketprice = 12.0
    elif milesvalue >= 20:
        ticketprice = 10.0
    elif milesvalue >= 10:
        ticketprice = 8.0
    else:
        ticketprice = 5.0
    return ticketprice


totalticketprice = 0.0

userresponse = input("Do you want to do this program (Yes or No): ")

while userresponse.lower() == "yes":
    lastnamevalue = input("Enter last name: ")
    milesvalue = float(input("Enter miles from downtown Chicago: "))

    ticketprice = CompTicketPrice(milesvalue)

    print(f"Last Name: {lastnamevalue}")
    print(f"Ticket Price: ${ticketprice}")

    totalticketprice = totalticketprice + ticketprice

    userresponse = input("Do you want to continue with this program? ")

print(f"Total Ticket Price: ${totalticketprice}")