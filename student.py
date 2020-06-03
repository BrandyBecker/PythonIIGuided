class Student:
    my_list = []

    def __init__(self, first_name, last_name): #we want info attached to the obj in memory
        self.first_name = first_name
        self.last_name = last_name
        Student.my_list.append(self)
    
    def __str__(self):
        return f"This student's name is {self.last_name}, {self.first_name}"

me = Student("Brandy","Becker")
print(me.my_list)

# "self" prints the class & object in memeory
# "__init__" requires an argument ("self")
# "self" is not a reserved word in python, you can call it whatever you want (we could call it "banana")(just a variable)