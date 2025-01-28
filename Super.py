# Super() = Function used in a child class to call methods from a parent class (Superclass).
#           Allows you to extend the functionality of the inherited methods.
#
# For each class in order to instaniate objects we'll require a constructor.
# Using the super class we no longer need to manually assign attributes to each constructor instead we call parent's constructor. 
# we set Up a Constuctor for the class "Shape" via function "def __init__".
# "self.color" & "self.is_filled" no longer has to be in each shape due to being in the Parent / Super Class.
# 
# 
#
class Shape:
    def __init__(self, color, is_filled):                   # Constuctor filled with Attributes for the class "Shape".
        self.color = color                                  # Attributes are defined as Actions, Characteristics, & functions for the class "Shape"
        self.is_filled = is_filled                          # They're assigned as a counter part of the Dunder Method "def __init__". Each attribute within the Tuple must be accompanied by an action via "self." and the equal "=" sign to complete the method (line 12 - 14). 

def describe(self):
    print(F"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init_(color, is_filled)
        self.radius = radius

def describe(self):
    super().describe():
    print(F"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
    

                                                             # We have many differences within these classes. But we use the Super class to fill the 
class Square(Shape):                                         # classes / objects with the attributes they have in common, utilizing less lines of code.
    def __init__(self, color, is_filled, width):
        super().__init_(color, is_filled)
        self.width = width

def describe(self):
    print(F"It is a square with an area of {self.width * self.width}cm^2")
    super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init_(color, is_filled)
        self.width = width
        self.height = height

def describe(self):
    print(F"It is a triangle with an area of {self.height * self.width / 2}cm^2")
    super().describe()
                                                               # Moving forward we create Objects from the classes to inherite their attributes. But we also have to provide its own attributes just like above to complete the method / function.
Circle = Circle("Green", True, 14)                             # (color: Any, is_filled: Any, radius: Any) To complete a Circle
Square = Square("Blue", True, 18)                              # We could even user keyword arguments "color="red", is_filled="True" for better readability"
Triangle = Triangle("Gold", True, 20, 44)

print(Triangle.color)
print(Triangle.is_filled)
print(f"{Triangle.width}cm")
print(f"{Triangle.height}cm")
