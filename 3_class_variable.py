class Employee:
    raise_amount = 1.05  # Class variable
    no_of_employee = 0

    def __init__(self, name, age, email, pay=50000):
        self.name = name
        self.age = age
        self.email = email
        self.pay = pay
        Employee.no_of_employee += 1 # increment the no_of_employee by 1 for each instance of the class and it's not dependent on instance

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Pay: {self.pay}")

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount # using class variable, same as self.pay = self.pay * Employee.raise_amount
    

# Print the class dictionary
print(Employee.__dict__)

employee1 = Employee('Md Fakrul Islam', 25, '98fakrulislam@gmail.com')
employee2 = Employee('Md Ruhul Amin', 20, 'ruhul.amin@gmail.com')
employee3 = Employee('Md Shakibul Islam', 30, 'shakibul.72@gmail.com')

# Print the instance dictionary
print(employee1.__dict__)
employee1.apply_raise()
print(employee1.raise_amount)
# see the pay after raise by dictionary
print(employee1.__dict__)


# set the raise amount for employee1 externally, and see the difference with class variable
# and how it was possible? because we have used self.raise_amount in apply_raise method instead of Employee.raise_amount 
# so, it is possible to set raise_amount for each employee separately
# this way, at first code looks for the attribute in instance, if not found then it looks for the attribute in class
employee1.raise_amount = 1.10
print(f'employee1.raise_amount : {employee1.raise_amount}')
print(f'employee2.raise_amount : {employee2.raise_amount}')
print(f'Employee.raise_amount : {Employee.raise_amount}')

# see the total number of employee
# explaination: no_of_employee is a class variable, so it is shared among all instances of the class
print(Employee.no_of_employee) # 3