# For Loops Jan 08, 2025
# For Loops = Execute a block of code a fixed number of times.
# You can iterate over a range, string, sequesnce, etc (anything iterable).

for x in range(1, 11):
    print(x)

print("Happy New Year!")

# reverse the range to count backwards / down via the reversed class

for x in reversed(range(1, 11)):
    print(x)
    
print("Happy New Year!")

# Add a "step" to specify by "how many" you'd like to complete the request observed as by 2 below:

for x in reversed(range(1, 11, 2)):
    print(x)
    
print("Happy New Year!")

# Simulate a Credit Card number.

credit_card = "1234-5678-9101-1004"

for x in credit_card:
    print(x)

print("Not moving on to Continue and Break")
print("Continue Example")

#useful key words = continue and break

for x in range (1, 21):
    if x == 13:
        continue
    else:
        print(x)

print("Break Example")

for x in range (1, 21):
    if x == 13:
        break
    else:
        print(x)

# Because we specified that if x == 13 we break. Once we reached "13" we broke out of the loop not continuing past "12"
