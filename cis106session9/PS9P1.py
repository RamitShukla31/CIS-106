#Last Name: Ramit Shukla  Date created: 3/29/2026

def CompForecast(monthvalue, salesvalue):
    if monthvalue in ["Jan", "Feb", "Mar"]:
        forecastpercent = 0.10
    elif monthvalue in ["Apr", "May", "Jun"]:
        forecastpercent = 0.15
    elif monthvalue in ["Jul", "Aug", "Sep"]:
        forecastpercent = 0.20
    elif monthvalue in ["Oct", "Nov", "Dec"]:
        forecastpercent = 0.25
    else:
        forecastpercent = 0.0

    nextsalesvalue = salesvalue * (1 + forecastpercent)
    return nextsalesvalue


userresponse = input("Do you want to do this program (Yes or No): ")

while userresponse.lower() == "yes":
    lastnamevalue = input("Enter last name: ")
    monthvalue = input("Enter month (Jan-Dec): ")
    salesvalue = float(input("Enter sales amount: "))

    nextsalesvalue = CompForecast(monthvalue, salesvalue)

    print(f"Last Name: {lastnamevalue}")
    print(f"Next Month Forecast: ${nextsalesvalue}")

    userresponse = input("Do you want to continue with this program? ")