#Last Name: Ramit Shukla  Date created: 5/3/2026

#Last Name: Ramit Shukla  Date created: 4/14/2026

class Student:
    def __init__(self, firstnamevalue, lastnamevalue, districtcode, creditsvalue):
        self.firstnamevalue = firstnamevalue
        self.lastnamevalue = lastnamevalue
        self.districtcode = districtcode
        self.creditsvalue = creditsvalue

    def ComputeTuition(self):
        if self.districtcode.upper() == "I":
            tuitionvalue = self.creditsvalue * 250.00
        else:
            tuitionvalue = self.creditsvalue * 500.00
        return tuitionvalue

    def DisplayStudent(self):
        tuitionvalue = self.ComputeTuition()
        print(f"Student Name: {self.firstnamevalue} {self.lastnamevalue}")
        print(f"District Code: {self.districtcode}")
        print(f"Credits Enrolled: {self.creditsvalue}")
        print(f"Tuition Owed: ${tuitionvalue:.2f}")


student1 = Student("Ramit", "Shukla", "I", 12)
student2 = Student("James", "abc", "O", 9)

student1.DisplayStudent()
print()
student2.DisplayStudent()