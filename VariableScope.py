#                                   Variable Scope - Jan 16, 2025

# Variable Scope = Where a avariable is visible and accessible
# Scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in


# def funct1():               # Within function 1 a = 1 
#     a = 1                   # Variables declared within a function have a LOCAL scope.
#     print(a)                # Remember funcitons cant see inside of other functions. Therfor funct2 CANNOT print a (& vice versa)
#                    Which is why we pass arguments to functions via fstrings{} so that our functions are aware of them. 
# def funct2():               # Within function 2 b = 2
#     b = 2
#     print(b)

# funct1()
# funct2()

# def funct1():
#     print(x)

# def funct2():
#     print(x)

# x = 3               # X is observed as a GLOBAL function bc it is outside of any function.
#                     when we run this program we get 3 twice because its called once for each function.
# funct1()            # There is no longer a local version of "x" for each of these fucntions.
# funct2()

from math import e

def funct1():
    print(e)

funct1()            # if we were to give e its own value such as 4 we create to different values for the variable.
#                     Variables can share the same name as long as they are within a different scope.
#                     There is now a built-in version of e as well as a global version.
#                     When printing e it would utilize the global version due to the LEGB (Scope Resolution Order).
#                     it first looks for Local, then Enclosed before it succefully finds a Global version.

