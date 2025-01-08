# WHILE LOOPS JAN 08 2025

# While Loop = Execute some code WHILE some specified Condition(s) remain True.

name = input("Enter your name: ")

while name == "":
    print("You did not type anything!")
    name = input("Enter your name: ")
else:
    print(f"Hello {name}!")

age = int(input("What is your age?: "))

while age < 0:
    print(f"Silly {name}, age can't be Negative!")
    age = int(input("What is your age?: "))
else:
    print(f"Wow you are {age} years old!")

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}.")
    food = input("Enter another food you like (q to quit): ")

print("Bye")

num = int(input("Enter a # between 1 - 100: "))

while num < 1 or num > 100:
    print(f"{num} is NOT valid!")
    num = int(input("Enter a # between 1 - 100: "))

print(f"Your number is {num}")

#WHILE LOOPS COMPLETED -  May be used to verify information.
