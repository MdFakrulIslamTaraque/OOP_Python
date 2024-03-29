class Employee:
    raise_amount = 1.05  # Class variable
    no_of_employee = 0   # class variable

    # by default, any method of a class is regular method
    # regular methods automatially takes instance as first argument, by convention it is 'self'
    def __init__(self, name, age, email, pay=50000):
        self.name = name
        self.age = age
        self.email = email
        self.pay = pay
        Employee.no_of_employee += 1 # increment the no_of_employee by 1 for each instance of the class and it's not dependent on instance

    def display(self, details):
        print(f"{details} : Name: {self.name} | Age: {self.age} | Email: {self.email} | Pay: {self.pay}")

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount # using class variable, same as self.pay = self.pay * Employee.raise_amount

    # now to create a class method, we need to use decorator @classmethod (decorator: a way to extend the functionality of a function or method)
    # class method takes class as first argument, by convention it is 'cls'
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # class method as alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        name, age, email = emp_str.split('-') # split the string by '-' and assign to name, age, email ( not to be confused with not putting with self, as in the next line, we are creating instance of the class and returning it)
        return cls(name, age, email) # return the instance of the class, same as Employee(name, age, email)
    
    # static method doesn't take instance or class as first argument, so it doesn't have 'self' or 'cls' as first argument
    # static method is used when we don't need to access instance or class variables
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: # 5 is saturday and 6 is sunday
            return False
        return True

# Inheritance: Creating a subclass from a superclass (parent class) and inherit all the attributes and methods of the parent class 
# and also can have its own attributes and methods
# here, Developer is a subclass of Employee and by this way, Developer can access all the attributes and methods of Employee 
class Developer(Employee):
    raise_amount = 1.10 # overriding the class variable of Employee class

    # use super() to call the __init__ method of Employee class along with the attributes of Developer class
    def __init__(self, name, age, email, pay=50000, prog_lang='Python'):
        super().__init__(name, age, email, pay)
        self.prog_lang = prog_lang

#creating instance of Developer and accessing the attributes and methods of Employee
employee1 = Developer('Md Fakrul Islam', 25, '98fakrulislam@gmail.com', 60000)

# here, display method is called from Employee class and Developer class doesn't have display method
# Its called Method Resolution Order (MRO) and it follows the order of inheritance
employee1.display("Developer")

# we can also see the Method Resolution Order (MRO) by using help function
# print(help(Developer))

# Check the attributes overrinding the class variable of Employee class
# here, raise_amount is overriden by Developer class
employee1.apply_raise()
employee1.display("Developer")

employee2 = Employee('Md Ruhul Amin', 20, 'ruhul.amin@gmail.com')
employee2.apply_raise()
employee2.display("Employee") # here, raise_amount is not overriden by Developer class

# Create another subclass of Employee named Maneger
class Manager(Employee):
    def __init__(self, name, age, email, pay=50000, employees=None):
        super().__init__(name, age, email, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def display_employee(self):
        for emp in self.employees:
            emp.display("Employee of {}".format(self.name))

manager1 = Manager('Tarek', 30, 'tarek@gmail.com', 70000, [employee1, employee2])
manager1.display("Manager")
manager1.display_employee()

manager1.remove_employee(employee1)
manager1.display_employee()

# Check the instance of the class
print(isinstance(manager1, Employee)) # True
print(isinstance(manager1, Developer)) # False
print(isinstance(manager1, Manager)) # True

# Check the subclass of the class
print(issubclass(Manager, Employee)) # True
print(issubclass(Manager, Developer)) # False
print(issubclass(Developer, Employee)) # True
print(issubclass(Employee, Developer)) # False