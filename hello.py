print("Hello, World")
answer = input("What's your name: ")
print("Hello, " + answer)

answer2 = int(input("What's your shoe size: "))
if answer2 > 10:
    print("Wow you have a big foot!")
elif answer2 < 6:
    print("Wow you have a small foot!")
else:
    print("Your shoe size is average.")

answer3 = int(input("How many pairs of shoes do you have: "))
if answer3 > 9:
    print("Wow, you have a lot of little shoes.")
elif answer3 < 5:
    print("Wow you only have", answer3, "pairs of shoes?")
else:
    print("That's an average amount of shoes")
