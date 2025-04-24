print("Hello World!")


# Strings
name = "Martian"
# Integers (Whole Numbers)
age = 36
# Float (Decimal Numbers)
height = 5.9

# Boolean (T or F)
is_student= True

print("Hey my name is " + name)
# print("Hey my name is", name) an alternative type of string concatination.
# *Via this comma method we DO NOT need to add a space after "is" NOR a "+" before "name" (space is auto added)

print(name[-1]) # Print the data located at -1 in the variable "name"

# Python is a case sensitive language so "Hello" & "hello" are different words.

message = "hello world!"
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.replace("l","L"))
print("World" in message)
print(len(message))

greeting1 = "Hello"
greeting2 = "hello"

# Conditions

if greeting1 == greeting2:
    print("They are the same!")
else:
    print("They are Different!")

# Type Conversions
age_str = "36"
age_num = int(age_str)
print(age_str)
print(type(age_num))
print(type(age_str))

price_float = 29.99
prince_int = int(price_float)
print(price_float)
print(type(price_float))
print(type(prince_int))
