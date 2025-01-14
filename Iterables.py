#                       Iterables in Python Jan 13, 2025
#Iterables = An object / collection that can return its elements one at a time, allowing to to be iterated over in a loop.

# numbers = [1, 2, 3, 4, 5]         # List
# numbers = (1, 2, 3, 4, 5)         # Tuple
# for number in numbers:
#     print(number)

# Will print our numbers one line at a time. May ever do so backwards / starting at the end using the reversed method.
# for number in reversed(numbers):
#     print(number)
# Print is a function. If you would rather not get each element of the output on a new line. 
#                      We can replace the new line character with the keyword argument end=" " OR end="-" 
#                      It can be WHATEVER you would liek to follow your elements with!

# SETS: Enclose any value(s) in the form of "strings" within a set of '{}'
# Sets ARE NOT reversable. Sets are also UNORDERED.

# fruits = {"apples", "bananas", "oranges", "kiwis", "watermelon"}

# for fruit in fruits:
#     print(fruit)


# STRINGS: An element enclosed within qoutations.

# name = "Martian"

# for character in name:
#     print(character, end=" ")

# Will print each character one by one veritically. If you would like to have them on the same line.
#                                                   We can replace the new line character with the keyword argument end=""
#                                                   (No Space within the qoutations) 

# DICTIONARIES: Key: Value pairs enclosed within an set of '{}'.

my_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4}

# for key in my_dictionary:
#     print(key)                             # Will return the keys of my_dictionary, but NOT the values!


# for value in my_dictionary.values():
#     print(value)                          # To get the values of my_dictionary, use the built in '.values()' method.


# for key, value in my_dictionary.items():
#     print(key, value)                            # To retirve BOTH the KEY & VALUE. we use the built in '.items()' method.
#                                                # Make sure both the Key and Value are separated by a comma.


for key, value in my_dictionary.items():
    print(f"{key} = {value}")                           # We can format the output however we'd like i.e an F string.
