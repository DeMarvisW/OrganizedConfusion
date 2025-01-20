#                       Multiple Inheritance & Multi-level Inheritance - JAN 18, 2025

# Multiple Inheritance = Inherit from more than one parent class.
#                        C(A, B)
# Multi-level Inheritance = Inherit from a parent which inherits from another parent.
#                           C(B) <- B(A) <- A 
#                           
# A -> B(A) -> (B)C
#
#
#
# class Animal:
#    def __init__(self, name):
#        self.name = name
#    def eat(self):
#        print("----------------------")
#        print("                      ")
#        print("This animal is eating.")
#        print("                      ")
#        print("----------------------")

#     def sleep(self):
#         print("------------------------")
#         print("                        ")
#         print("This animal is sleeping.")
#         print("                        ")
#         print("------------------------")


# class Prey(Animal):
#   def flee(self):
#        print("-----------------------")
#        print("                       ")
#        print("This animal is fleeing.")
#        print("                       ")
#        print("-----------------------")


# class Predator(Animal):
#     def hunt(self):
#         print("-----------------------")
#         print("                       ")
#         print("This animal is hunting.")
#         print("                       ")
#         print("-----------------------")


# class Rabbit(Prey):
#    def flee(self):
#        print("--------------------------------------------------")
#        print("                                                  ")
#        print("The rabbit is fleeing, it's frieghtened but quick.")
#        print("                                                  ")
#        print("--------------------------------------------------")

        
# class Hawk(Predator):
#     def hunt(self):
#         print("-----------------------------------------")
#         print("                                         ")
#         print("The hawk is hunting from high in the sky.")
#         print("                                         ")
#         print("-----------------------------------------")


# class Fox(Predator):
#     def hunt(self):
#         print("-------------------------------------------------")
#         print("                                                 ")
#         print("The fox is a sly one, it hunts while you're away.")
#         print("                                                 ")
#         print("-------------------------------------------------")


# class Fish(Prey, Predator):
#     def hunt(self):
#         print("-----------------------------------------------------")
#         print("                                                     ")
#         print("The fish are hunting, while fleeing from bigger FISH.")
#         print("                                                     ")
#         print("-----------------------------------------------------")


# rabbit = Rabbit("Peter")       
# hawk = Hawk("Tony")               
# fish = Fish("Jaws")          
# fox = Fox("Reggie")                 

# Prey to Rabbit object. "(we can also assign our object a name as observed)".
# Predator to Hawk object.
# Predator & Prey to Fish object.
# Predator to Fox object.

# fish.eat()





class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("----------------------")
        print("                      ")
        print(f"{self.name} is eating.")
        print("                      ")
        print("----------------------")

    def sleep(self):
        print("------------------------")
        print("                        ")
        print(f"{self.name} is sleeping.")
        print("                        ")
        print("------------------------")


class Prey(Animal):

    def flee(self):
        print("-----------------------")
        print("                       ")
        print(f"{self.name} is fleeing.")
        print("                       ")
        print("-----------------------")


class Predator(Animal):

    def hunt(self):
        print("-----------------------")
        print("                       ")
        print(f"{self.name} is hunting.")
        print("                       ")
        print("-----------------------")


class Rabbit(Prey):

    def flee(self):
        print("----------------------------------------------------------")
        print("                                                          ")
        print(f"{self.name} Rabbit is fleeing, he's frieghtened but quick.")
        print("                                                          ")
        print("----------------------------------------------------------")

        
class Hawk(Predator):

    def hunt(self):
        print("--------------------------------------------")
        print("                                            ")
        print(f"{self.name} is hunting from high in the sky.")
        print("                                            ")
        print("--------------------------------------------")


class Fox(Predator):

    def hunt(self):
        print("-------------------------------------------------------------")
        print("                                                             ")
        print(f"The fox {self.name} is a sly one, it hunts while you're away.")
        print("                                                             ")
        print("-------------------------------------------------------------")


class Fish(Prey, Predator):

    def hunt(self):
        print("------------------------------------------------------------------------")
        print("                                                                        ")
        print(f"{self.name} and his pack are hunting, while fleeing from bigger SHARKS.")
        print("                                                                        ")
        print("------------------------------------------------------------------------")


rabbit = Rabbit("Peter")       
hawk = Hawk("Tony")               
fish = Fish("Jaws")          
fox = Fox("Reggie")                 

# Prey to Rabbit object. "(we can also assign our object a name as observed)".
# Predator to Hawk object.
# Predator & Prey to Fish object.
# Predator to Fox object.

fish.hunt()
