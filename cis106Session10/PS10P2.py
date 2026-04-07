#Last Name: Ramit Shukla  Date created: 4/6/2026

def CompExamStats(scoreone, scoretwo, scorethree):
    totalpoints = scoreone + scoretwo + scorethree
    averagevalue = totalpoints / 3
    return totalpoints, averagevalue


studentlastname = input("Enter student last name: ")
scoreone = float(input("Enter exam score 1: "))
scoretwo = float(input("Enter exam score 2: "))
scorethree = float(input("Enter exam score 3: "))

totalpoints, averagevalue = CompExamStats(scoreone, scoretwo, scorethree)

print(f"Student Last Name: {studentlastname}")
print(f"Total Points: {totalpoints:.2f}")
print(f"Average Score: {averagevalue:.2f}")




