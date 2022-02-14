class Employee():

    raise_amount = 1.20
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

emp_1 = Employee("Abdul", "Malek", 30000)
emp_2 = Employee("Afridi", "Saheen", 40000)

# emp_str_1 = 'Sifat-Hamidi-30000'

# new_emp_1 = Employee.from_string(emp_str_1)

#Employee.set_raise_amt(1.05)

# print(new_emp_1.email)

import datetime
mydate = datetime.date(2022,2,6)
print(Employee.is_workday(mydate))


