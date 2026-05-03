#Last Name: Ramit Shukla  Date created: 5/3/2026


class Employee:
    def __init__(self, firstnamevalue, lastnamevalue, addressvalue, cityvalue, statevalue, zipvalue, employeeid, salaryvalue):
        self.firstnamevalue = firstnamevalue
        self.lastnamevalue = lastnamevalue
        self.addressvalue = addressvalue
        self.cityvalue = cityvalue
        self.statevalue = statevalue
        self.zipvalue = zipvalue
        self.employeeid = employeeid
        self.salaryvalue = salaryvalue

    def DisplayEmployee(self):
        print(f"Employee ID: {self.employeeid}")
        print(f"Name: {self.firstnamevalue} {self.lastnamevalue}")
        print(f"Address: {self.addressvalue}, {self.cityvalue}, {self.statevalue} {self.zipvalue}")
        print(f"Salary: ${self.salaryvalue:.2f}")


emp1 = Employee("Ramit", "Shukla", "123 Main St", "Chicago", "IL", "60000", 101, 75000)

emp1.DisplayEmployee()