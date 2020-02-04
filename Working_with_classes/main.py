class Employee:

    raise_amount = 1.05
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    def full_name(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Prasang', 'Biyani', 50000)
emp2 = Employee('Test', 'Testing1', 60000)

print(Employee.__dict__)
print(emp1.raise_amount)
Employee.raise_amount = 1.08
print(emp1.raise_amount)
print(emp2.raise_amount)

print(Employee.num_of_emps)

