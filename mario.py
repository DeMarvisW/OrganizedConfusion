#defined a function named main() including what it should do once called upon.
def main():
    height = get_height()
    for i in range(height):
        print("#")

#Defined the parameters within that function and what action they take when called upon ex: get_height()
def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                return n
        except ValueError:
            print("Not an integer")
#Call the function that has been defined so that when the code is excuted the parameters are enabled.
main()

#Named Argument observed below.
for i in range(4):
    print("?", end="")
print()
