class Employee:

    raise_amount=1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay=int(self.pay* self.raise_amount)

emp_1 = Employee('Joseph', 'thachil', 50000)
emp_2 = Employee('Paul', 'Varghese', 60000)

print(emp_1.first, emp_1.last)
print(emp_1.email)
print(emp_2.email)
print(emp_1.pay)
print(emp_2.pay)
print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.raise_amount)
emp_1.apply_raise()
print(emp_1.pay)
emp_2.raise_amount=1.09
print(emp_2.raise_amount)
print(emp_2.pay)
