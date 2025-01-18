#                                    Object Oriented Programming (OOP) - Jan 18, 2025

# Object =  a "bundle" of related attributes (variables) and methods (functions).
#           EX: phone, cup, book.
#           You need a class to create objects.
# Class = (Blueprint) Used to design the structure and layout of an object. What an object has and can do.
# This is a dunder method (double underscore) we need this method to contruct an object. 
# It behaves similarly to a function. Will be required to set parameters within () following "self".
# Self refers to the object that we're creating rn now (Car).
# Model = (str) String BMW
# Year = (Int) Number 
# Color = (str) String Green
# For_sale = Bool (Yes / No) (True / False)
# Printing Car1 (print(Car1)) would print the object and the location of where it is found within our memory.
# I.e: <__main__.Car object at 0x72f4368efd70>
# Therefore we must simutaneously call an attribute i.e: print(Car1.model)
# The observed DOT(.) prior to the attribute model is know as the ATTRIBUTE ACCESS OPERATOR.

# Classes may take up alot of space / Memory so we can create a new Python file via:
# File > New >> Python File >>> Create Name >>>> Input your desired info.
# Upon doing so we call call the class within any workspace via Importing it via:
# "from" "Created Name" "import" "Class"

# Within our Class we can create functions / Methods / actions that our class can perform.

from Car import Car
from Car import DeMarvis
# (From the file Car.py we imported the Class "Car")

Car1 = Car("CTS", 2025, "Black", True)
Car2 = Car("ATS", 2025, "White", True)
Car3 = Car("XTS", 2025, "Olive", True)


# print(Car1.model)
# print(Car1.color)
# print(Car1.for_sale)

# Car1.describe()
# Car2.describe()




DeMarv_is_TheMartian = DeMarvis("Queer", 35, "Underweight", "Coily Haired", "Non-binary")

# print(Martian.age)
# print(Martian.gender)

DeMarv_is_TheMartian.appearance()
DeMarv_is_TheMartian.Martian()
