#                                   INHERITANCE - JAN 18, 2025

# Inheritance = Allows a class to inherit attributes and methods from another class. 
#               Helps with code reuseability and extensibility.
#               Class Child(Parent)
#                          ^ AKA Sub(Super) classes

# class Father:
#     Height = 5'8
#     Color = "Black"

# class Son(Father):
#     pass

class Animal:                                       # Create a class: Animal.
    def __init__(self, name):                     # Define the constructor, and pass in a name.
        self.name = name
        self.is_alive = True

    def eat(self):                                  # All animals can eat.
        print(F'{self.name} is eating.')            # print using an string

    def sleep(self):
        print(F"{self.name} is sleeping.")

class Dog(Animal):           # This Dog class will inherit all of the methods and attributes from its parent class (Animal).
    def speak(self):         # Children classes can also have their own individual attributes. 
        print(f"WOOF!")

class Cat(Animal):           # This Cat class will inherit all of the methods and attributes from its parent class (Animal).
    def speak(self):
        print(F"MEOW!")

class Mouse(Animal):         # This Mouse class will inherit all of the methods and attributes from its parent class (Animal).
    def speak(self):
        print(F"SQEAK!")

dog = Dog("Ollie")           # Here we create a Name attribute for the class Dog. 
cat = Cat("Chelsea")         # Here we create a Name attribute for the class Cat.
mouse = Mouse("Mickey")      # Here we create a Name attribute for the class Mouse.

print(dog.name)
print(dog.is_alive)
dog.eat()                   # Here we have our dog OBJECT use the eat METHOD.
dog.sleep()                 # Here we have our dog OBJECT use the sleep METHOD.

print(cat.name)
print(cat.is_alive)
cat.eat()                    # Here we have our cat OBJECT use the eat METHOD.
cat.sleep()                  # Here we have our cat OBJECT use the sleep METHOD.

print(mouse.name)
print(mouse.is_alive)
mouse.eat()                  # Here we have our mouse OBJECT use the eat METHOD.
mouse.sleep()                # Here we have our mouse OBJECT use the sleep METHOD.

dog.speak()                  # Here we have our dog OBJECT use the speak METHOD.
cat.speak()                  # Here we have our cat OBJECT use the speak METHOD.
mouse.speak()                # Here we have our mouse OBJECT use the speak METHOD.

