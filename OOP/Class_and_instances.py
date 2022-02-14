class Employee():

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com"
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee("Abdul", "Malek", 800)
emp_2 = Employee("Afridi", "Saheen", 750)

print(emp_2.email)
print(emp_2.fullname())
#print(Employee.fullname(emp_1))