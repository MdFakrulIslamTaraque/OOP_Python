# creating an empty class, without error by using 'pass'
class Employee:
    pass

# crating object of the empty class
employee1 = Employee()
employee2 = Employee()


# creating class attributes externally
employee1.Name = 'Md Fakrul Islam'
employee1.Age = 25

employee2.Name = 'Md Ruhul Amin'
employee2.Age = 20

# But this naive way is cumbersome to set attributes for each employee and also error prone
# We should use constructor to set this iitially
print(f"employee1's Name : {employee1.Name} | Age: {employee1.Age}\nemployee2's Name : {employee2.Name} | Age: {employee2.Age}")