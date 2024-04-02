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

    # generally, printing any object returns the memory location of the object, which is neither useful for developers nor for end users
    # To make it useful, __repr__ and __str__ methods can be used, which returns a string representation of the object
    # while creating a class, __repr__ and __str__ methods can be used to return a string representation of the object
    # at least __repr__ method should be used, as it is used for debugging, if __str__ method is not used, then __repr__ method will be used
    # __repr__ method is used to return a string representation of the object, which can be used for debugging -> for developers
    def __repr__(self):
        return f"Employee('{self.name}', {self.age}, '{self.email}', {self.pay})"
    
    ## __str__ method is used to return a string representation of the object, which can be used for end users -> for end users
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    # some self created magic/dunder methods
    # __len__ method is used to return the length of the object (like list, tuple, string etc.)
    def __len__(self):
        return len(self.name)
    
    # overloads the '+ operator' for the object of the class
    # __add__ method is used to add two objects of the class
    def __add__(self, other):
        return self.pay + other.pay
        
        
    # overloads the '+ operator' for the object of the class
    # __add__ method is used to add two objects of the class
    def __sub__(self, other):
        return self.pay - other.pay
    
emp_1 = Employee('Md Fakrul Islam', 25, '98fakrulislam@gmail.com', 60000)
print(emp_1) # here, we the __str__ method is called, if __str__ method is not used, then __repr__ method will be called, if both of them are not used, then it will return the memory location of the object


## normally len() function is used to get the length of an object like list, tuple, string etc.
## but if we want to get the length of an object of a class, then we can use __len__ method
print(len(emp_1))


emp_2 = Employee('Md Ruhul Amin', 20, 'ruhul.amin@gmail.com')
print(emp_2)
print(emp_1 + emp_2) # here, we the __add__ method is called
print(emp_1 - emp_2) # here, we the __sub__ method is called