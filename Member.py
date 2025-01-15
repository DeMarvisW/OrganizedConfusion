#                       Membership Operators  Jan 13, 2025

# Memebership Operators = Are used to test wether a value or variable is found within a sequence
#                         (Strijng, List, Tuple, Set, or Dictionary)
#                         1. in
#                         2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}") 
