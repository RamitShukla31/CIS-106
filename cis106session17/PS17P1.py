#Last Name: Ramit Shukla  Date created: 5/11/2026

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

    def computelongtermbonus(self):
        longtermbonus = self.pay * 0.40
        return longtermbonus


class Executive(Manager):

    def __init__(self, first, last, pay, bonusrate, employees=None):
        super().__init__(first, last, pay, bonusrate, employees)

    def ExecutiveBonus(self):
        executivebonus = self.pay * 2.00
        return executivebonus

    def computelongtermbonus(self):
        longtermbonus = self.pay * 0.50
        return longtermbonus


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python', 0.10)
dev_2 = Developer('Test', 'Employeee', 60000, 'Java', 0.15)

mgr_1 = Manager('Sue', 'Smith', 90000, 0.20, [dev_1])

exec_1 = Executive('Tony', 'Stark', 150000, 0.25, [dev_1, dev_2])

print(exec_1.fullname())
print(exec_1.email)

bonusamount, totalcompensation = exec_1.computebonus()

print(f"Bonus Amount: ${bonusamount:.2f}")
print(f"Total Compensation: ${totalcompensation:.2f}")

print(f"Executive Bonus: ${exec_1.ExecutiveBonus():.2f}")

print(f"Long Term Bonus: ${exec_1.computelongtermbonus():.2f}")

exec_1.print_emps()