#                                          Duck Typing - Feb 09, 2025
#                                                                                                                                 # Duck typing - Another way to achieve Polymorphism besides inheritance
#                                                                                                                                 # Objects can be treated as if they were a different Type as long as they have the minimum neccessary Attributes / Methods. As long as an object resemnbles another it can be treated as that Type.
#                                                                                                                                 # From the expression "If it looks like a Duck and Quacks like a Duck, it must be a duck."

class Animal:                                                                                                                     # Here we create a Class named Animal. We give it an "alive" attribut and set it to "True".
    alive = True

class Dog(Animal):                                                                                                                # We create a Class named "Dog(Animal)" and via inserting Animal we set it to inherit all the Actions / Methods / Functions of Animal.
    def speak(self):
        print("WOOF!")


class Cat(Animal):                                                                                                                # With OOP we created an Object via creating a Class named Cat that is an (animal)
    def speak(self):                                                                                                              # Gave it a Method to "speak". A Function it (self) does when the speak(Method) is called.
        print("MEOW.")                                                                                                            # To speak for this object is to Print "MEOW." when called. 


class Car:
    def speak(self):
        print("Honk!")

    alive = False

animals = [Dog(), Cat(), Car()]                                                                                                          # Creat a List[] of "animals" via constructing a Dog(object) & Cat(object) and placing inside Square Brackets.

for animal in animals:                                                                                                            # For every animal in the List[] animals:
    animal.speak()                                                                                                                #                                         Use the speak(Method).
    print(animal.alive)                                                                                                           #                                         Print the "alive" Attribute.                        
