import sys

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

name = input("Name: ")

for n in names:
    if name == n:
        print("Found")
        sys.exit(0)

print("Not Found")
sys.exit(1)


#Alternatively we can simplify via removing the for loop via line 7

import sys

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

name = input("Name: ")

if name in names:
        print("Found")
        sys.exit(0)

print("Not Found")
sys.exit(1)
