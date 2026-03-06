#Last Name: Ramit Shukla  Date created: 3/3/2026

UserResponse = input("Do you want to run this program: ")

while UserResponse.lower() == "yes":

    firstNumber = 1
    secondNumber = 1

    print(firstNumber)
    print(secondNumber)

    for count in range(3, 21):
        nextNumber = firstNumber + secondNumber
        print(nextNumber)
        firstNumber = secondNumber
        secondNumber = nextNumber

    UserResponse = input("Do you want to run this loop again? ")

    




