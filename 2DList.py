# 2 Dimensional List Jan 09 2025
# A two dimensional list is a list made of list.
# 2D List = [[List], [List], [List]]

# fruits =     ["apples", "oranges", "pineapple", "watermelon"]
# vegetables = ["carrots", "peas", "brocolli", "cauliflower"]
# meats =      ["chicken", "beef", "pork", "turkey"]

# groceries = [fruits, vegetables, meats]
# To access elements of a 2D list you require to indices (groceries[0][0]) as one would return the entire row
# print(groceries)

# Telephone Number Pad Using 2D tupple.

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:           # For every row in the tupple "Num Pad"
    for num in row:           # & For every number in the row
        print(num, end=" ")   # Print the numbers, then end the line.
    print()
