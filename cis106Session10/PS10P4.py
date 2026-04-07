#Last Name: Ramit Shukla  Date created: 4/6/2026

def CompBowlerStats(scoreone, scoretwo, scorethree, handicapvalue):
    totalpoints = scoreone + scoretwo + scorethree
    averagevalue = totalpoints / 3
    averagewithhandicap = averagevalue + handicapvalue
    return averagevalue, averagewithhandicap


bowlerlastname = input("Enter bowler last name: ")
scoreone = float(input("Enter game score 1: "))
scoretwo = float(input("Enter game score 2: "))
scorethree = float(input("Enter game score 3: "))
handicapvalue = float(input("Enter handicap: "))

averagevalue, averagewithhandicap = CompBowlerStats(
    scoreone, scoretwo, scorethree, handicapvalue
)

print(f"Bowler Last Name: {bowlerlastname}")
print(f"Average Score: {averagevalue}")
print(f"Average with Handicap: {averagewithhandicap}")