class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Joseph', 'thachil', 50000)
emp_2 = Employee('Paul', 'Varghese', 60000)

print(emp_1.first, emp_1.last)
print(emp_1.email)
print(emp_2.email)
print(emp_1.pay)
print(emp_2.pay)
print(emp_1.fullname())
print(emp_2.fullname())