import math
x = 10
y = 5

print("x = 10")
print("y = 5")
print("==============")
print("x + y =")
print(x+y)
print("==============")
print("x - y =")
print(x-y)
print("==============")
print("x / y =")
print(x/y)
print("==============")
print("x * y =")
print(x*y)
print("==============")
print(x%y)
print("==============")
print(x**y)

print("==============")
# x = x + 15
x += 15
print("x += 15 =")
print(x)

#String Operations - The observed format of first UNDERSCORE last is known as "Snake Script"

first_name= "Martian"
last_name= "AmongMen"
full_name= first_name + " " + last_name
print(first_name, last_name)
print(full_name)

print("Hey my name is " + first_name + " and my last name is " + last_name)

# F Strings - Used for convience as it does NOT require the + for concatination.

print(f"Hey my name is {first_name} and my last name is {last_name}.")

# int floor division

a = 17
b = 5
print("=================================")
print("a // b =")
print(a // b) # Result 3 (rounds down) 17 / 5 is normally 3.4
print("a / b =")
print(a / b)
print("=================================")

# Assigning Multiple values
i, j, k = 1, 2, 3
print(i, j, k)

# Swap Values
m = 10
n = 20
m, n = n, m
print(m, n)

# Comparison Operators
c = 5
d = 10
print("=================================")
print("C = 5", "D = 10")
print("=================================")
print("Is C equal to D?")
print(c ==  d)
print("=================================")
print("Is C NOT equal to D?")
print(c != d)
print("=================================")
print("Is C greater than D?")
print(c > d)
print("=================================")
print("Is C less than D?")
print(c < d)
print("=================================")
print("Is C greater than or equal to D?")
print(c >= d)
print("=================================")
print("Is C less than or equal to D?")
print(c <= d)
print("=================================")

# Logical Operators
a = True
b = False

print(a and b) # Returns False bc BOTH are NOT "True"
print(a or b)  # Returns True bc ONE is accurate
print(not a)   # Returns False bc you are printing what A is NOT
print(not b)   # Returns True bc you are printing what B is NOT
print("=================================")
# String Slicing
text = "Python Programming"
print(text[0:6])   # Print all of the data obsrved in "text" from 0-5
print(text[7:])
print(text[::-1])  # Print all of the data in text BUT in REVERSE
print("=================================")
# String Formatting with .format()
name = "Alice"
age = 25
msg = "My name is {} and I am {} years old".format(name,age)
print(msg)
print("=================================")

# Using Placeholders
msg2 = "My name is {0} and I am {1} years. {0} is a nice name".format(name,age)
print(msg2)
print("=================================")

# Math Module Operations

print(math.pi)
print(math.sqrt(16))
print(math.floor(4.7))   # Round Down to 4
print(math.ceil(5.3))    # Round Up to 6
print(math.pow(2,3))     # 2 to the power of 3

pi = 3.141592653589793   # Define pi as a float observed as the provided
print(round(pi,2))       # instruct the system to print pi to the 2nd decimal placement when printing pi
print("=================================")
