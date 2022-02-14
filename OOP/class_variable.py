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

emp_1 = Employee("Abdul", "Malek", 30000)
emp_2 = Employee("Afridi", "Saheen", 40000)

print(Employee.employee_number)

print(emp_1.pay)
print(emp_2.pay)

emp_1.apply_raise()

print(emp_1.pay)
print(emp_2.pay)
