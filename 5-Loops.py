# For Loops

#print("Counting from 1 to 5:")
#for i in range(1, 6):
#    print(i)

#print("\nCounting in reverse from 5 to 1:")
#for i in range(5, 0, -1):
#    print(i)

# While Loops

#count = 1
#print("While Loop")  # while count is <= 5 Starting at count (1). Print the count + 1 until equal to 5 
#while count <= 5:
#    print(count)
#    count += 1

# Reverse the While Loop

#count = 5
#print("\n Reversed While Loop")  # while count is >= 1 Starting at count (5). Print the count - 1 until equal to 1 
#while count >= 1:
#    print(count)
#    count -= 1


# Looping through a List

fruits = ["apple", "banana", "cherry"]
#print("My Fruit:")
#for fruit in fruits:
#    print(fruit)


# Looping through a List in reverse

#print("\nMy fruits in reverse:")
#for fruit in reversed(fruits):
#    print(fruit)

# List enumerated

#print("fruit with indices:")
#for index, fruit in enumerate(fruits):
#    print(f"{index}:{fruit}")

# Loop with Dictionaries

#person = {"name": "Martian", "age": "36", "city": "Austin"}
#print("Person Dictionary")
#for key, value in person.items():
#    print(f"{key}:{value}")

# List Comprehension (Compact loop for creating List)

#squares = [x**2 for x in range(1,6)]   #[1,4,9,16,25]
#print("Squares from 1 to 5", squares)

# For Loop with Zip()

#colors = ["red", "yellow","green"]
#for fruit,color in zip(fruits,colors):
#    print(f"{fruit} is {color}")

#Break and Continue

#print("Loop with break")
#for i in range(1,10):
#    if i > 5:
#        break
#    print(i)

#print("\nLoop with Continue")
#for i in range(1, 10):
#    if i % 2 == 0:
#        continue    # skip even numbers
#    print(i)

# Infinite Loops with break condition

i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break
