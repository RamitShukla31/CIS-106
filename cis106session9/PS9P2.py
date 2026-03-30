#Last Name: Ramit Shukla  Date created: 3/29/2026

import math

def CompSquareFootage(lengthvalue, widthvalue, heightvalue):
    floorceiling = 2 * lengthvalue * widthvalue
    wallone = 2 * lengthvalue * heightvalue
    walltwo = 2 * widthvalue * heightvalue

    squarefootage = floorceiling + wallone + walltwo
    return squarefootage


userresponse = input("Do you want to do this program (Yes or No): ")

while userresponse.lower() == "yes":
    lengthvalue = float(input("Enter room length: "))
    widthvalue = float(input("Enter room width: "))
    heightvalue = float(input("Enter room height: "))

    squarefootage = CompSquareFootage(lengthvalue, widthvalue, heightvalue)

    gallonsneeded = squarefootage / 50
    gallonsneeded = math.ceil(gallonsneeded)

    print(f"Square Footage: {squarefootage}")
    print(f"Gallons of Paint Needed: {gallonsneeded}")

    userresponse = input("Do you want to continue with this program? ")