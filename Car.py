class Car:
    def __init__(self, model, year, color, for_sale):  
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print(f"You drive the {self.color} {self.model}")
#                              Self refers to the object that we are currently working with.
    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

class DeMarvis:
    def __init__(self, adjective, age, physic, hair_color, gender):
        self.adjective = adjective
        self.age = age
        self.physic = physic
        self.hair_color = hair_color
        self.gender = gender

    def Martian(self):
        print("You will be a Master Programmer!")
    
    def appearance(self):
        print(f"A {self.adjective} {self.age} {self.physic} {self.hair_color} {self.gender} that will no doubt conquer all in his path")
    
