# Default Arguments = A default value for certain parameters.
#                     A default is used when an argument is ommitted.
#                     They make your functions more flexible & reduces the number of arguments. 
# Types of arguments = 1. Positional 2. DEFAULT  3. Keyword  4. Arbitrary

# def net_price(list_price, discount, tax):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500, 0, 0.05))
# Equals 525.0

# We can also set our parameters to have a default value via:

# def net_price(list_price, discount=0, tax=0.05):
#    return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))

# The above can also accept up to two additional arguments. i.e a 10% discount:
# When printing the arguement for our discount we use what is passed in rather than the default. observed in line 14

# print(net_price(500, .1))  
# Equals 472.5

# print(net_price(500, .1, 0))  # The same can be applied for sales tax. 
                                # We use what is passed in rather than the default. observed in line 14


#                        CREATE A COUNT TIMER USING DEFAULT ARGUMENTS


import time         # Import Time module.
def count(start, end):      # Create a function named count, containing 2 arguments.
    for x in range(start, end+1):       # Create a for loop. The 2nd argument is exclusive so we add 1 to the end of our time.
        print(x)                        # we have a start/end point that increments by 1 moving upward due to +1. 
        time.sleep(1)                # Make the program sleep for a give amount of time before continuing via the sleep method.
    print("DONE!")                   # Following the for loop / upon completion. We'll print "DONE!"

count(0, 10)            # invoke the function via calling it with parameters of your choice passed in MUST BE 2 (start & end).
