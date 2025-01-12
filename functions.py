# Function =  a block of reusable code
#             place () after the function's name to invoke it.

# Define a function = "def" + "Create a Name" + parenthesis followed by : 
# Any code that belongs to function you'll be required to indent underneath.

# def Happy_Birthday(name, age):
#    print(f"Happy birthday to {name}!")
#    print(f"You are {age}")
#    print(f"Happy birthday to {name}!")
#    print()

# To invoke the function you type the name of the function with parenthesis i.e: Happy_Birthday()
# Using whats called an argument you can send data directly to a function.
# via placing a parameter within the function (a temp variable):
# In order to invoke you need a matching number of arguments. Can't have only one but attempt to invoke two.

# def Happy_Birthday("One", 2):
#    print("Happy birthday to {name}!")
#    print("how old are you?")
#    print("Happy birthday to you!")
#    print()
# happy_Birthday("Martian", 35)

# Happy_Birthday("Martian", 35)



# Create an invoice

# def display_invoice(name, amount, due):
#     print(f"Hello {name}")
#     print(f"you bill of ${amount} is due on {due}")

# display_invoice("Martian", 100, "1/2025")

# print() 

#                                    RETURN

# Return Statement = A statement used to enda a function and send a result back to a caller.

#def add(x, y):
#    z = x + y
#    return z

#def subtract(x, y):
#    z = x - y
#    return z

#def multiply(x, y):
#    z = x * y
#    return z

#def divide(x, y):
#    z = x / y
#    return z

#print(add(1, 2))
#print(subtract(1, 2))
#print(multiply(1, 2))
#print(divide(1, 2))

def create_name(first, last):      # Function to create a full name. #2 these are our paramenters.
    first = first.capitalize()         # Capitalize #3 We took those values and made them uppercase.
    last =  last.capitalize()
    return first + " " + last           # We would like to return a first and last name with a space between when invoked.
                                            #4 We concatinated the strings together.
full_name = create_name("Martian", "Williams")      #1 Create a variable named full_name. We sent our function some arguments.

print(full_name)   #5 Using the "return" statement you can recall some data back to the plase in which you call a function.
