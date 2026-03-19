#Last Name: Ramit Shukla  Date created: 3/18/2026

def CompTuition(credithours, districtcode):
    if districtcode == "I":
        tuitionrate = 250.0
    elif districtcode == "O":
        tuitionrate = 550.0
    else:
        tuitionrate = 0.0

    tuitionvalue = credithours * tuitionrate
    return tuitionvalue


totaltuition = 0.0
studentcount = 0

userresponse = input("Do you want to do this program (Yes or No): ")

while userresponse.lower() == "yes":
    studentlastname = input("Enter student last name: ")
    credithours = float(input("Enter credit hours: "))
    districtcode = input("Enter district code (I or O): ").upper()

    tuitionvalue = CompTuition(credithours, districtcode)

    print(f"Student Last Name: {studentlastname}")
    print(f"Tuition Owed: ${tuitionvalue}")

    totaltuition = totaltuition + tuitionvalue
    studentcount = studentcount + 1

    userresponse = input("Do you want to continue with this program? ")

print(f"Total Tuition Owed: ${totaltuition}")
print(f"Total Students Entered: {studentcount}")