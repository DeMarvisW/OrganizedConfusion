#                                         Polymorphism - Feb 5, 2025
from abc import ABC, abstractmethod                                                                                               # To work with Abstract Classes we need to Import the built-in Super() FUNCTION, (A decorator indicating abstract methods).
#                                                                                                                                 # Polymorphism - Greek word meaning "To have many forms or faces."
#                                                                                                                                 # Poly - Many
#                                                                                                                                 # Morphe -Form
#
#                                                                                                                                 # TWO WAYS TO ACHIEVE POLYMORPHISM
#                                                                                                                                 # 1. Inheritance - An object could be treated of the same Type as a parent Class. 
#                                                                                                                                 # 2. Duck typing - Object must have neccesary Attributes / Methods.

class Shape:

    @abstractmethod                                                                                                               #  Preceeding the "area" Method we added an Abstract method decorator via '@' + 'the abstract Method built-in FUNCTION' (Hover for additional info). 
    def area():
        pass

#                                                                                                                                 # The following Shapes (Objects) have two forms (i.e A Circle is both a Circle and a "Shape".)

class Circle(Shape):
    def __init__(self, radius):
#       super().__init__()
        self.radius = radius



class Square(Shape):
    def __init__(self, side):
#       super().__init__()
        self.side = side



class Triangle(Shape):
    def __init__(self, base, height):
#       super().__init__()
        self.base = base
        self.height = height


#                                   Observing Polymorphism Using List[]!

# Create a List[] that includes our Shape OBJECTS and Name it accordingly refer to the following:

shapes = [Circle(), Square(), Triangle()]



