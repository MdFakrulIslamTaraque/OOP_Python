# creating class with constructor to set attributes initially
class Employee:
    # constructor to set attributes initially
    def __init__(self, name, age, email) -> None:
        self.Name = name
        self.Age = age
        self.Email = email
    
    # method to display employee details
    def display(self):
        # using self to access class attributes
        return f"Name: {self.Name} | Age: {self.Age} | Email: {self.Email}"

# crating object of the class with constructor
employee1 = Employee('Md Fakrul Islam', 25, '98fakrulislam@gmail.com')
employee2 = Employee('Md Ruhul Amin', 20, 'ruhul.amin@gmail.com')

#print(f"employee1's Name : {employee1.Name} | Age: {employee1.Age}\nemployee2's Name : {employee2.Name} | Age: {employee2.Age}")

# instead of above print statement each time, we can use display method to display employee details
# here every instance of the class will be used as self parameter
# this is same as Employee.display(employee1) and Employee.display(employee2)
print(employee1.display())
print(employee2.display())