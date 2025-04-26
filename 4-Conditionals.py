# Python uses indentations to define blocks of code, not curly brackets or other symbols

#print("=================================")
#temp = 45
#if temp > 80:
#    print("it's hot outside.")
#elif temp > 70:
#    print("it's a nice day outside.")
#else:
#    print("It's Cold outside.")
#
#print("=================================")

# Checking Multiple Conditions with logical operators

# age = 13
# has_license = True

# if age >= 16 and has_license:
#    print("You can drive a car.")
#elif age <= 15 and not has_license:
#    print("You need to obtain a driver's licence.")
#else:
#    print("You are not old enough to drive a car.")

# Nested Conditionals

#print("=================================")
#score = 100

#if score >= 60:
#    print("You Passed.")
#    if score >= 90:
#        print(f"Your score is {score}%")
#        print("You got an A.")
#    elif score >= 80:
#        print(f"Your score is {score}%")
#        print("You got a B ")
#    elif score >= 70:
#        print(f"Your score is {score}%")
#        print("You got a C")
#    else:
#        print(f"Your score is {score}%")
#        print("You got a D")
#else:
#    print(f"Your score is {score}%")
#    print("Unfortunately, you Failed!")
#
#print("=================================")

# Using the "in" operator in conditionals

#fruit = "apple"
#if fruit in ["apple", "pear", "orange"]:
#    print(f"{fruit} is in the list.")
#else:
#    print(f"{fruit} is not observed in the list.")
#
# Ternary Operator (A one-line if-else statement.)

#age = 45
#status = "Adult" if age >= 18 else "Minor"
#print(f"You are {age} you are a {status}.")

#print("=================================")

# Compare Strings

#password = "secret123"
#if password == "secret123":
#    print("Access Granted")
#else:
#    print("ACCESS DENIED!!")

#Chaning Comparisons
#print("=================================") 
#x = 15
#if 10 < x < 20:
#    print("x is between 10 and 20")

# Truthful or Falsified
print("=================================") 
user_input = ""
if user_input:
    print("Input Provided.")
else:
    print("No input has been provided!")
print("=================================") 
