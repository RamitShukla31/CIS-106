#Last Name: Ramit Shukla  Date created: 2/22/2026

UserResponse = input("Do you want to run this program: ")

while UserResponse.lower() == "yes":

    PrincipleAmount = float(input("Enter Principal Amount: "))
    InterestRate = float(input("Enter Interest Rate: "))

    accumulatedInterest = 0.0

    for year in range(1, 6):
        beginningbalance = PrincipleAmount
        interest = beginningbalance * InterestRate
        endingBalnace = beginningbalance + interest
        accumulatedInterest = accumulatedInterest + interest

        print(f"Year: {year}")
        print(f"Beginning balance: ${beginningbalance}")
        print(f"Ending balance: ${endingBalnace}")

        PrincipleAmount = endingBalnace

    print(f"Accumulated Interest: ${accumulatedInterest}")

    UserResponse = input("Do you want to run this loop again? ")



