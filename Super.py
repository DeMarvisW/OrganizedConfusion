# Super() = FUNCTION used in a Child class (Subclass) to call methods from a Parent class (Superclass).
#           Allows you to extend the functionality of the inherited methods.
#
# For each class in order to instaniate objects we'll require a constructor.
# Using the super class we no longer need to manually assign attributes to each constructor instead we call parent's constructor. 
# Observed we set Up a Constuctor for the class "Shape" via the function "def __init__".
#  "self.color" & "self.is_filled" NO LONGER has to be in each individual shape due to being in the Parent / Super Class.
# 
# 
class Shape:                                                # In order to instantiate objects we require a Constructor for each class.
    def __init__(self, color, is_filled):                   # Constuctor filled with Attributes / Parameters for the class "Shape".
        self.color = color                                  # Attributes / Parameters are defined as Actions, Characteristics, & functions for the class. Ex:"Shape" when referring to our observed code.
        self.is_filled = is_filled                          # They're "Assigned" as a counter part of the Dunder Method "def __init__". Each attribute within the Tuple must be accompanied by an action via "self." and the equal "=" sign to complete the method (line 12 - 14). 

    def describe(self):                                     # We can also extend the functionality of a method. Within our Shape class. We can create a METHOD named describe. It will have the attributes / Parameters of "Shape" via "describe(self):".
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")                                                       #


#                   Now Circle, Square, & Triangle will have access to the FUNCTION "describe(self):"


class Circle(Shape):                        
    def __init__(self, color, is_filled, radius):       # The Child class (Subclass) inherited the Parent class' (Superclass) Attributes / Parameters. We can call upon them via the Super() FUNCTION. 
        super().__init__(color, is_filled)              # Within this constructor of the Child / Sub class. We have to call the Constructor for the Parent class via the Super() Function. Observed as indented beneath this class's Constructor. 
        self.radius = radius                            # The Parent class "Shape" doesn't have a radius Attribute so we must Assign one via "self. & =". As it's required for the class "Circle" which is being constructed (created via the Constructor).
#                                                       # Super() Functions allows us to eliminate lines of code for readability and time. As Inheritance can be utilized. (Observe how we're no longer required to include the "self.color" & "self.is_filled" lines within the Circle Object / Class.)

    def describe(self):
        print(F"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()
    

#                                                        # We have many differences within these classes. But we use the Super class to fill the classes / objects with the Attributes / Parameters they have in common, utilizing less lines of code.
class Square(Shape):                                     # "METHOD Overiding" utilizes the Child class' attributes over the Parents
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled) 
        self.width = width                               # To extend the functionality of a Method from the the Super / Parent Class we can use the Super() FUNCTION. 
#                                      

    def describe(self):
        print(f"It is a Square with an area of {self.width * self.width}cm^2")
        super().describe()                              



class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled) 
        self.width = width
        self.height = height
#                                                                         
    def describe(self):
        print(f"It is a Triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()                                                 # Via the Super() FUNCTION we can use the describe Method from both the child and parent. Within the child class' FUNCTION (indented beneath "def describe(self):) # Observed in this line the Super() FUNCTION that we are calling from this objects Super / Parent class is the "describe()" FUNCTION.
#                                                                          # Moving forward we create Objects from the classes to inherite their Attributes / Parameters. But we also have to provide its own Attributes / Parameters just like above to complete the method / function.
#                                                                          # (color: Any, is_filled: Any, radius: Any) To complete a Circle, Square & Triangle.
#                                                                          # We could even user keyword arguments "color="red", is_filled="True" for better readability"
Circle = Circle(color="Green", is_filled=True, radius=14)                  
Square = Square(color="Blue", is_filled=True, width=18)                    
Triangle = Triangle(color="Gold", is_filled=True, width=20, height=44)


# Triangle.describe()                                                      # To call / use a METHOD (Action) you simply call the Object (Class Name) DOT METHOD (i.e 'Triangle.describe()')
#                                                                          # By Doing so the functions within the Class will be executed.
