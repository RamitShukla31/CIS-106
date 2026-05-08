#Last Name: Ramit Shukla  Date created: 5/7/2026

class Employee: 
    raise_amt = 1.04

    def __init__(self, first, last, pay, bonusrate):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.bonusrate = bonusrate

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def computebonus(self):
        bonusamount = self.pay * self.bonusrate
        totalcompensation = self.pay + bonusamount
        return bonusamount, totalcompensation


class Developer(Employee):
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang, bonusrate):
        super().__init__(first, last, pay, bonusrate)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, bonusrate, employees=None):
        super().__init__(first, last, pay, bonusrate)

        if employees is None: 
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())        


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python', 0.10)
dev_2 = Developer('Test', 'Employeee', 60000, 'Java', 0.15)

mgr_1 = Manager('Sue', 'Smith', 90000, 0.20, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

print(dev_1.email)
print(dev_2.prog_lang)

bonusamount, totalcompensation = dev_1.computebonus()

print(f"Bonus Amount: ${bonusamount:.2f}")
print(f"Total Compensation: ${totalcompensation:.2f}")