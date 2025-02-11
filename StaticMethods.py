#                                         Static Methods - Feb 10, 2025                                                           # Static Methods - Best for utility functions that do not need access to class data.  
#                                                                                                                                 # Methods that belongs to a class rather than any object from that class (instance). Used for general utility functions.
#                                                                                                                                 #  
#                                                                                                                                 # @staticmethod                                                                        
#                                                                                                                                 # def km_to_miles(kilometers):
#                                                                                                                                 #     return kilometers * 0.621371
#                                                                                                                                 #
#                                                                                                                                 # Inatance Methods - Best for operations on instances of the class (objects).
#                                                                                                                                 #
#                                                                                                                                 # def get_info(self):
#                                                                                                                                 #     return f"{self.name} = {self.position}"
class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):                                                                                                           # Instance Method - A Method that belongs to an instance of a class and operates on instance attributes. It takes "self" as the first parameter, which represents the instance of the class. 
        return f"{self.name} = {self.position}"                                                                                   # Each object we create from this class will have their own "get_info" instance method to return the information on that object (The name and position).
    


    @staticmethod                                                                                                                 # To create a static method we need a decorator. We can use this Method to design a methdo to see if position
    def is_valid_position(position):                                                                                              # Static Methods DONT have "self" as the first arguement. Because we're NOT working with any objects created from "Employee" Class. We dont have to rely on any objects to use this method.
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]                                                               # We created a function / defined a "Method" named "is_valid_position" and passed in an arguement "position"
        return position in valid_positions                                                                                        # We then created a List[] w various positions named "valid positions".


employee1 = Employee("Eugene", "Manager")
employee2 = Employee("squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(Employee.is_valid_position("Cook"))                                                                                         # With a Static Method you only need to access the class (Employee). You don't even need to create any objects from that class
print(employee1.get_info())                                                                                                       # For an instance method you access an object (employee1) then call the instance method (get_info())
print(employee2.get_info())                                                                                                       # Returns True if located within our list. Otherwise returns False.
print(employee3.get_info())                                                                                                       #
