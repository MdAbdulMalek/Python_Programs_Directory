class Employee():

    raise_amount = 1.05
    employee_number = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com"
        self.pay = pay

        Employee.employee_number +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, p_lan):
        super().__init__(first, last, pay)
        self.p_lan = p_lan

class Manager(Employee):
    def __init__(self, first, last, pay, employess = None):
        super().__init__(first, last, pay)
        if employess is None:
            self.employess = []
        else:
            self.employess = employess
    
    def add_emp(self, emp):
        if emp not in self.employess:
            self.employess.append(emp)

    def remove_emp(self, emp):
        if emp in self.employess:
            self.employess.remove(emp)

    def print_emps(self):
        for i in self.employess:
            print("-->", i.fullname())

dev_1 = Developer("Abdul", "Malek", 30000, 'RUBY')
dev_2 = Developer("Afridi", "Saheen", 40000, 'Python')

#dev_1.apply_raise()

man_1 = Manager("Naim", "Sarker", 80000, [dev_1])

# print(dev_1.email)
# print(dev_1.p_lan)

# print(man_1.email)
# man_1.add_emp(dev_2)
# man_1.print_emps()
#print(dev_1.p_lan)

# print(emp_1 + emp_2)

# print(len(emp_1))
