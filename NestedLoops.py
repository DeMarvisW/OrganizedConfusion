# JAN 08 2025
# Nested Loop = A loop within another loop (outer, inner)
# Outer Loop:
#     Inner Loop:

rows = int(input("Enter the number of rows: "))
colomns = int(input("Enter the number of colomns: "))
symbols = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(colomns):
        print(symbols, end=" ")
    print()
