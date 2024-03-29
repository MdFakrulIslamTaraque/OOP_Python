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

    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | Email: {self.email} | Pay: {self.pay}")

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


# set the raise amount for all employees using class method
Employee.set_raise_amount(1.10)

# set the employee detils using the alternative constructor 
employee4 = Employee.from_string('Md Rakibul Alam-23-rakibul@gmail.com')
employee4.apply_raise()
print(employee4.display())

# check if it is workday or not using static method
import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date)) # False