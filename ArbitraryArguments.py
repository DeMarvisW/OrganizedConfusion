#                                   Arbitrary Arguments JAN 12, 2025
# Arbitrary = A varying amount of arguments.
# *args     = Allows you to pass multiple non-key arguments (TUPLE).
# **kwargs  = Allows you to pass multiple keyword arguments {DICTIONARY}.
#           * Unpacking operator
#           1. Positional 2. Default 3 Keyword 4. ARBITRARY


# Python supports two main types of Arbitrary arguements: 

# *args: For non-keyworded variable length arguments.              

# **kwargs: For keyworded variable length arguments.
#               
# *args                                            **kwargs
# -------                                          -----------
# 1, 2, 3                                          key1=value1  key2=value2
# Tuple                                            Dictionary
# Non-keyword Arguments                            Keyword Arguments


# USING *ARGS
# The *args syntax allows you to pass a variable number of POSITIONAL arguments to a function.

# EXAMPLE:
# def sum_number(*args):
#     return sum(args)
# print(sum_numbers(1, 2, 3))  # Output: 6

# HOW *ARGS WORK
# Input to sum_numbers(1, 2, 3)          
# args = (1, 2, 3)                          # Which is a Tuple
# 
# Process:
# 1 + 2 + 3 = 6
# Output: 6                                 # Which is the sum of the nunbers observed within the Tuple


# USING *KWARGS
# The **kwargs syntax allows you to pass a variable number of KEYWORD arguments which are stored as a DICTIONARY.

# EXAMPLE:
# def display_info(*args, **kwargs):
# print("Positional Arguments:", args)
# print("Keyword Arguments:", kwargs)
#
# display_info(1, 2, 3, names="Kyle", age="35")


# COMBINING *ARGS & **KWARGS:
# input to display_info(1, 2, 3, names="Kyle", age="35"):
# args = (1, 2, 3)
# kwargs = {"names":"Kyle", "age":"35"}
#
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {"names": "Kyle", "age": "35"}

# ORDER OF PARAMETERS w *ARGS & **KWARGS
# 
# When defining a function, the parameters must follow this order:
#
# 1. Positional Arguments
# 2. Default Arguments
# 3. *Args
# 4. **Kwargs
#
# EXAMPLE:
# def example(a, b=10, *args, **kwargs):
# print(a, b, args, kwargs)
# example(1, 20, 30, 40, name="Kyle")
#
# PARAMETER ORDER:
# Input to example(1, 20, 30, 40, name="Kyle"):
# a = 1
# b = 20
# args = (30, 40)
# kwargs = {"name": "Kyle"}
#
# Output:
# 1 20 (30, 40) {"name": "Kyle"}
#
# UNPACKING w *ARGS & **KWARGS
# You can use * and ** to unpack list, tuples, or dictionaries when calling a function.
#
# EXAMPLE:
# def greet(name, age):
#     print(f"Hello {name}! You are {age} years old.")
# date = {"name": "Kyle", "age": 35}
# greet(**data)
#
#UNPACKING w **KWARGS
# Input to greet(**{"name": "Kyle", "age": 35}):
# name = "Kyle"
# age = 35
#
# OUTPUT:
# Hello, Kyle! You are 35 years old.
#
#
#
# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#
#     if "apt" in kwargs:
#         print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#     elif "pobox" in kwargs:
#         print(f"{kwargs.get('street')}")
#         print(f"{kwargs.get('pobox')}")
#     else:
#         print(f"{kwargs.get('street')}")
#
#    print(f"{kwardgs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}") 
#     
# Shipping_label("Dr.", "Kyle", "Williams",
#                street="123 Fake St.",
#                apt="#100",
#                city="Austin",
#                state="Texas",
#                zip="54321")
# 
#               
#               
#               
#
#                                    Arbitrary Arguments JAN 12, 2025
# Arbitrary = A varying amount of arguments.
# *args     = Allows you to pass multiple non-key arguments (TUPLE).
# **kwargs  = Allows you to pass multiple keyword arguments {DICTIONARY}.
#           * Unpacking operator
#           1. Positional 2. Default 3 Keyword 4. ARBITRARY

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")

# print_address(street="123 Baldwin St",
#               city="Hutto",
#               state="Texas",
#               zip="78634")

# print_address


