# Super() = FUNCTION used in a Child class (Subclass) to call methods from a Parent class (Superclass).
#           Allows you to extend the functionality of the inherited methods.
#
# For each class in order to instaniate objects we'll require a constructor.
# Using the super class we no longer need to manually assign attributes to each constructor instead we call parent's constructor. 
# we set Up a Constuctor for the class "Shape" via function "def __init__".
# "self.color" & "self.is_filled" no longer has to be in each shape due to being in the Parent / Super Class.
# 
# 
#
class Shape:                                 # In order to instantiate objects we require a Constructor for each class.
    def __init__(self, color, is_filled):                   # Constuctor filled with Attributes / Parameters for the class "Shape".
        self.color = color                                  # Attributes / Parameters are defined as Actions, Characteristics, & functions for the class. Ex:"Shape" when referring to our observed code.
        self.is_filled = is_filled                          # They're "Assigned" as a counter part of the Dunder Method "def __init__". Each attribute within the Tuple must be accompanied by an action via "self." and the equal "=" sign to complete the method (line 12 - 14). 

def describe(self):                         # We can also extend the functionality of a method. Within our Shape class we can create a METHOD named describe. It will have the attributes / Parameters of "Shape" via "describe(self):".
    print(F"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):       # The Child class (Subclass) inherited the Parent class' (Superclass) Attributes / Parameters. We can call upon them via the Super() FUNCTION. 
        super().__init__(color, is_filled)               # Super() Functions allows us to eliminate lines of code for readability and time. As Inheritance can be utilized. (Observe how we're no longer required to include the "self.color" & "self.is_filled" lines within the Circle Object / Class.)
        self.radius = radius                            # The Parent class "Shape" doesn't have a radius Attribute so we must Assign one via "self. & =". As it's required for the class "Circle" which is being constructed (created via the Constructor).

def describe(self):
    super().describe()
    print(F"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
    

#                                                        # We have many differences within these classes. But we use the Super class to fill the classes / objects with the Attributes / Parameters they have in common, utilizing less lines of code.
class Square(Shape):                                     # The Child (Subclass) will utilize the Childs atributes over the parents unless told otherwise via "Method" Overiding.
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled) 
        self.width = width

def describe(self):
    print(F"It is a square with an area of {self.width * self.width}cm^2")
    super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled) 
        self.width = width
        self.height = height

def describe(self):
    print(F"It is a triangle with an area of {self.height * self.width / 2}cm^2")
    super().describe()
#                                                         # Moving forward we create Objects from the classes to inherite their Attributes / Parameters. But we also have to provide its own Attributes / Parameters just like above to complete the method / function.
Circle = Circle("Green", True, 14)                        # (color: Any, is_filled: Any, radius: Any) To complete a Circle, Square & Triangle.
Square = Square("Blue", True, 18)                         # We could even user keyword arguments "color="red", is_filled="True" for better readability"
Triangle = Triangle("Gold", True, 20, 44)

print(Circle.color)
print(Circle.is_filled)
print(f"{Circle.radius}cm")
