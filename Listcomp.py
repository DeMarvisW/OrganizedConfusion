#                               List Comprehension - Jan 15, 2025

# List COmprehension = A precise way to create List in Python.
#                      More compact and easier to read than traditional loops.
#                      [expression for value in iterable if condition]

#                                   TRADITIONAL LOOP EXAMPLE:


# doubles = []                   # The variable "doubles" equal an empty list.
# for x in range(1, 11):         # In a range function the second # is excluded meaning this list ends at 10.
#     doubles.append(x * 2)      # For the numbers(x) in the range of 1 - 10 (11 is excluded).
#                                  Multiply each number by 2 and add them to the "doubles" list[].
# print(doubles)                   which before was empty. Essentially creating a new list: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].


#                                   LIST COMPREHENSION EXAMPLE: LOOPS

# We will follow the formula: [Write the expression for a value in this iterable optionally we can check a condition.]

# doubles = [x * 2 for x in range(1, 11)]    # doubles = [expression for value in iterable]
#                           # The expression is what would we like to do with x? (double it / multiple it by 2)
# print(doubles)              # Our list[] named doubles = the number * 2 for every number in the range of 1 - 10.

# triples = [y * 3 for y in range(1, 11)]

# print(triples)

# squares = [z * z for z in range(1, 11)]

# print(squares)


#                                LIST COMPREHENSION: STRINGS

# fruits = ["Apples", "Bananas", "Kiwis", "Oranges", "Pears","Watermelon"]
# fruits = [fruit.upper() for fruit in fruits] 
# print(fruits)

# We can cut down on the steps required via removing the 1st line and integrating it into the 2nd line for less lines of code:

# fruits = [fruit.upper() for fruit in ["Apples", "Bananas", "Kiwis", "Oranges", "Pears","Watermelon"]] 
# print(fruits)

# This NOW states that the variable "fruits" is = the uppercase version of EVERY "fruit" in this provided List[].

# Whereas before we deifined a list and used the list's name to accomplish this.

# Now let's take each fruit and create a new list containing only their first letter using indexing.

# fruits = ["Apples", "Bananas", "Kiwis", "Oranges", "Pears","Watermelon"]
# fruit_chars = [fruit[0] for fruit in fruits]   # fruit_chars = For every fruit in out list of fruits
# print(fruit_chars)                             # return the first character of each string.


#                                           CONDITIONS:

# POSITIVE NUMBERS:
# numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10] # Create a list comprehension where we create a new list w all pos numbers.
# pos_numbers = [num for num in numbers if num >= 0] # If our value of num meets the condition 
#                                                          return it and place it within a newly created List[].
# print(pos_numbers)                                 # ">= 0" causes our program to ONLY print the positive numbers in our list.


# NEGATIVE NUMBERS:
# numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10] # Create a list comprehension where we create a new list w all neg numbers.
# neg_numbers = [num for num in numbers if num < 0] # If our value of num meets the condition 
#                                                          return it and place it within a newly created List[].
# print(neg_numbers)                                 # "< 0" causes our program to ONLY print the negative numbers in our list.


# EVEN NUMBERS:
# numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10] # Create a list comprehension where we create a new list w all even numbers.
# even_numbers = [num for num in numbers if num % 2 == 0] # If our value of num meets the condition 
#                                                          return it and place it within a newly created List[].
# print(even_numbers)                        # "% 2 == 0" causes our program to ONLY print the numbers in our list divisible by 2.


# ODD NUMBERS:
# numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10] # Create a list comprehension where we create a new list w all odd numbers.
# odd_numbers = [num for num in numbers if num % 2 == 1] # If our value of num meets the condition 
#                                                          return it and place it within a newly created List[].
# print(odd_numbers)                      # "% 2 == 1" causes our program to ONLY print the numbers in our list NOT divisible by 2.

#PASSING GRADES
grades = [85, 42, 70, 98, 87, 100, 75, 29]
passing_grades = [grade for grade in grades if grade >= 60]
# passing_grads = a grade of any grade in the list "grades" if that grade is >= 60
print(passing_grades)

#FAILING GRADES
grades = [85, 42, 70, 98, 87, 100, 75, 29]
failing_grades = [grade for grade in grades if grade < 60]
# failing_grads = a grade of any grade in the list "grades" if that grade is < 60
print(failing_grades)
