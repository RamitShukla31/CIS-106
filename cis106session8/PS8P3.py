#Last Name: Ramit Shukla  Date created: 3/17/2026

def CompMilesPerGallon(milestraveled, gallonsused):
    if gallonsused == 0:
        mpgvalue = 0.0
    else:
        mpgvalue = milestraveled / gallonsused
    return mpgvalue


tripcount = 0

userresponse = input("Do you want to do this program (Yes or No): ")

while userresponse.lower() == "yes":
    destinationcity = input("Enter destination city: ")
    milestraveled = float(input("Enter miles traveled: "))
    gallonsused = float(input("Enter gallons used: "))

    mpgvalue = CompMilesPerGallon(milestraveled, gallonsused)

    print(f"Destination City: {destinationcity}")
    print(f"Miles Traveled: {milestraveled}")
    print(f"Miles Per Gallon: {mpgvalue}")

    tripcount = tripcount + 1

    userresponse = input("Do you want to continue with this program? ")

print(f"Total number of trips entered: {tripcount}")
