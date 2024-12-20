# Concession Stand Program
# Dictionary: {"key":value}

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}
cart = []
total = 0

# For every key and value in our dictionary titled "menu" the ".items" returns a key and a value during each iteration.
# After each key i provided a format specifier of 10 decimals which adds 10 spaces between the key & value
# After value, using a format specifier I display 2 decimal places to account for the cents via ".2f"

print("-------------MENU-------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------------")

# Use a while loop to ask the user for "input" on which item they would like to buy from the menu.
# Specify that q is used to quit. If what you input for food is equal to q you break out of the while loop.
# ".lower" takes our input and makes it lowwercase in the even a user types an Uppercase Q.
# Else if (elif) for if a user types in a key / item no on the list.
# Use get method. If menu.get() entering "food" which is the users input. If it is not in our menu as a key it will return None / Nothing.
# We can achieve the above via "is not None". Our code state that if the food is there than append it to the cart. Otherwise dont add to cart.

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------YOUR ORDER-----------")

for food in cart:
    total += menu.get(food)
    print(food, end=", "),

print()
print(f"Total is: {total:.2f}")
