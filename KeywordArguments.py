# JAN 12, 2025
# Keyword Arguments = An argument proceeded by an Identifier.
#                     Helps with readability.
#                     Order of arguments doesn't matter
#                     1. Positional 2. Default 3. KEYWORD 4. Arbitrary

# def hello(greeting, title, first, last):                # Observed we defined a function named "hello".
#     print(f"{greeting} {title} {first} {last}")  # We told this function what to do. Print arguments you input as an f string.

# hello("Hello", "Mr", "Martian", "The Marvelous")    # When invoking this function it prints the arguments you input.

# Keyword arguemnts = hello("Hello", title="Mr", first="Martian", last="Among Men")
# Via inserting keyword arguments you can arrange theese in any order and they still are displayed correctly when called.
# Because we DIDN'T use a keyword on "Hello" it is a POSITIONAL argument.
# Positional arguments MUST come before keyword arguemnts when paired to avoid an error.

# Next let's print the numbers 1 - 10 using a "For Loop":

# for x in range(1, 11): 
#     print(x)            # After each print statement we print a new line meaning each number will be displayed on it's own line.
#                                    If we would like the numbers displayed on the same line we must follow x w a ',' 'end=" "'
#                                    Via adding the comma "end with a space", we tell the system NOT to continue via a new line 
#                                           BUT to contiue on same line following a space instead.
#     "end" is a "KEYWORD" Argument auto applied to the "print" function that tells the system to go to a new line.
#      We tell the system NOT to go to a new line but instead end w a space, presenting our output onto the same line.


#      Same can be said for the "Separate" Function.
#      Ex: print("1", "2", "3", "4", "5", "6" sep="*")
#      We can use the Separate keyword argument 'sep=" "' to separate these strings / numbers by whatever we want. 

# NEXT WE CREATE  A FUNCITON TO GENERATE A PHONE NUMBER.

def get_phone(country, area, first, last):  # Define the function as a set of arguments we input.
    return f"{country}-{area}-{first}-{last}"   # Set it to return an f string that matches the name of the functions parameters.

phone_num = get_phone(country=1, area=123, first=456, last=7890)
# ^ Create a variable that invokes your created function (The order doesn't matter when using Keyword arguments).
print(phone_num)    #When you print. You get the designated numbers in the designated order.
