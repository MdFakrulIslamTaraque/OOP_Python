class Employee:
    raise_amount = 1.05  # Class variable
    no_of_employee = 0   # class variable

    # by default, any method of a class is regular method
    # regular methods automatially takes instance as first argument, by convention it is 'self'
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    # property decorator is used to define a method as an attribute
    #usecase : if we want to access a method as an attribute, then we can use property decorator, some situation where, initially we have created a class property as an attribute, but later we want to change it as a method, then we can use property decorator
    @property
    def email(self):
        return f"{self.firstName}.{self.lastName}@gmail.com"

    @property
    def full_name(self):
        print(f"{self.firstName} {self.lastName}")
    
    # setter method is used to set the value of a method, 
    # if we want to set a method as an attribute using property delimeter, then we can use setter method
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.firstName = first
        self.lastName = last

    # deleter method is used to delete the value of a method
    @full_name.deleter
    def full_name(self):
        print('Delete Name!')
        self.firstName = None
        self.lastName = None


emp_1 = Employee('fakrul', 'islam')

emp_1.full_name # here, we can call it as an attribute, if we use property decorator
emp_1.full_name = "hello there" # but a method with property decorator can't be set as an attribute until we use setter method
emp_1.full_name # here, we can set the value of the method just like an attribute, only if we use setter method

del emp_1.full_name # here, we can delete the value of the method just like an attribute, only if we use deleter method
emp_1.full_name 

# print(emp_1.email()) # here, we are calling email as a method, but we can call it as an attribute, if we use property decorator
print(emp_1.email) # here, we are calling email as an attribute, if we use property decorator