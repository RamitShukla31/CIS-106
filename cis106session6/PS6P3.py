#Last Name: Ramit Shukla  Date created: 2/22/2026

userResponse = input("Do you want to run this program: ")

StudentCount = 0

while userResponse == "Yes":
    LastName = input("Enter you last name: ")
    ExamScore1 = float(input("Enter Exam score1: "))
    ExamScore2 = float(input("Enter Exam score2: "))

    averageScore = (ExamScore1 + ExamScore2)/2

    #print last name
    print(f"Student Last Name: {LastName}")
    #print averageScore
    print(f"Average Score: {averageScore}")

    StudentCount =  StudentCount + 1

    userResponse = input("Do you want to enter another student? ")

#print total student entered
print(f"Total Student Entered: {StudentCount}")

 