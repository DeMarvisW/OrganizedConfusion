# Class Vraiables = Shared among all ijnstances of a class.
#                   Defined outside of the constructor.
#                   Allow you to share data among all objects created from that class.
#______________________________________________________________________________________________________
#EXAMPLE:
# Class Car:
#                                  
#     wheels = 4                       <- This is referred to as a "Class Veriable. Located OUTSIDE of the constructor."
#                                         They allow sharing data among ALL objects created from that class.
#                                         Class Obsects share ONE variable.
#     def __init__(self, model, year):
#         self.model = model           
#         self.year = year             <-   These are referred to as "Instance Variables."
#                               (^ Instance / objects created from a class & located INSIDE the constructor. ^)
#                                           Each object has their own variable.
#_______________________________________________________________________________________________________

class Student:

    class_year = 2025
    num_students = 0                        # Variable created to keep track of the number of students we create.

    def __init__(self, name, age):          # Constructor within this section we can write any code
        self.name = name                    # we want this code will always be executed when we instantiate an object.
        self.age = age
        Student.num_students += 1           # To take our num of Students and increase it by 1 each time we construct a new student / object.
#                                           If we want to modify a class variable we use the name of our class variable INSTEAD of SELF
#                               ^ Access the Class of "Student" GET the "num_students" and INCREASE it by one.

student1 = Student("DeMarvis", 35)
student2 = Student("Bob", 35)
student3 = Student("Elijah", 12)
student4 = Student("Jayla", 11)

# print(student1.name)
# print(student1.age)
# print(student2.name)
# print(student2.age)

# print(Student.class_year)               # Here we are accessing the Class Variable via the Class itself (Student).
#                                         Rather than form one of the instances / students (student1 / student2).

# print(Student.num_students)             # Returns 4

print(f"The Python Graduating Class of {Student.class_year} is only {Student.num_students} Graduates!")
print(student1.name)
print(student2.name) 
print(student3.name) 
print(student4.name)
# ^ We printed the students Graduating year and class size using an Fstring and print statement. ^
