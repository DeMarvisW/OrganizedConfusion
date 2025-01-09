# Collections = A Single "variable" used to store multiple values
# List = [] Ordered and changeable. Duplicates are okay.
# Set = {} Unordered and imutable, but Add / Remove is okay. No duplicates.
# Tuple = () Ordered and Unchangeable. Duplicates are okay. Faster

# Below "fruits" is a variable observed as a list. Printing "fruits" will print the whole list.
fruits = ["apple", "orange", "banana", "watermelon"]

# However using [Indexing] we can print a single item from the list. apple = [0], orange = [1], banana = [2], and watermelon = [3]
# print(fruits[:2]) <- Would print apple - banana. Can use a step to print every other via print(fruits[::2])

# You can also iterate over Collections using a "for loop" as observed below. Would print each fruit.
# for fruit in fruits:
#     print(fruit)

# To lsit the different methods available to a function use the "dir()" method via print(dir(fruits)).
# For a description of each attribut and method available use the "help()" function via print(help(fruits)).
# For the length of how many elements are in a collection use the "len()" function via print(len(fruits)).
# using the "in" operatior we can find if an object / value is in our collection via print("apple" in fruits) returns a bool.
# Can iterate over / change a value via indexing i.e fruits[0] = "pineapple". Changes apple in our list to pineapple.
# Add an element to the end of the list via the append method i.e fruits.append(pineapple)
# To remove an element you can use the remove method. i.e fruits.remove("apple")
# Using the insert method you can insert a value at a give index. i.e fruits.insert(0, pineapple). *Inserts pineapple at 0.
# The sort method will sort our list into ABC order via fruits.sort.
# To reversea  list you would use the reverse method. fruits.reverse. Displays list in reverse.
# To reverse the list in ABC order first use sort followed by reverse. i.e fruits.sort() => fruits.reverse()
# to clear a list you can use the clear method. i.e fruits.clear().
# return the index of a value / element via the index method. i.e print(fruits.index("apple")) would return 0 
# Count the amount of times an element / value is found within a list via the count method. i.e print(fruits.count("apple"))

# You're unable to use indexing on a {}set bc a set is Unordered. 
