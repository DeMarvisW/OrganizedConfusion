#                       Membership Operators  Jan 13, 2025

# Memebership Operators = Are used to test wether a value or variable is found within a sequence
#                         (String, List, Tuple, Set, or Dictionary)
#                         1. in
#                         2. not in


#                                       STRINGS

# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

# word = "APPLE"

# For the inverse (The Letter is NOT in) we would be required to flip the If & ELSE statements i.e:

# letter = input("Guess a letter in the secret word: ")

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}") 

#                                              SETS
#
# STRINGS to SETS - Still utilizing strings. However they are now grouped as a collection found within a set of {}.

# students = {"DeMarvis", "Kyle", "Martian", "Bob"}

# student = input("Enter the name of a student: ")

# if student in students:
#     print(F"Yes, {student} is attending your lecture.")
# else:
#     print(f"No, {student} is not attending your lecture.")


# For the inverse (The Letter is NOT in) we would be required to flip the If & ELSE statements i.e:

# students = {"DeMarvis", "Kyle", "Martian", "Bob"}

# student = input("Enter the name of a student: ")

# if student not in students:
#     print(f"No, {student} is not attending your lecture.")
# else:
#     print(F"Yes, {student} is attending your lecture.")


#                                           Dictionaries
# Again utilizing {}. However they are now a collection of strings as a "KEY": paired w a ': "VALUE"' found within a set of {}.
# We press enter after each "Key": Value pair to ensure readability.

# grades = {"DeMarvis": "C", 
#           "Kyle": "A+", 
#           "Martian": "D", 
#           "Bob": "B"}


# student = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is a {grades[student]}")   # When we find student we have to get the value of the given key.
# else:                                                   # If we indeed find the "student" we receive the value of that key.
#     print(f"{student} was not found")                   # Otherwise we receive this fstring / line.


email = "DeMarvis@GMail.com"

if "@" in email and "." in email:           # We have 2 conditions check if @ is in email and . to confirm as a valid email.
    print("This email is Valid.")
else:
    print("This email is invalid!")   # In the example we are checking 2 conditions. If the "@" is found w/in the email variable.
 #                                      AND if a "." is found within the "email" variable.
