#            If __name__ == __main__ Dunder Statements - Jan 17, 2025

# Dunder = Double Underscore.
# print(dir()): brings up all attributes found within python (attributes are special types of variables).
# If we were to print(__name__) it would return dunder main (__main__)
# Which is why in a script you may see the statement if __name__ == "__main__" then you call a function named main() to start
# If we want to import a program: from program import * (* simply means to import EVERYTHING)
# If __name__ == __main__: (This script can be imported OR run stand alone.)
#                          Function and Classes in this Module can be reused without the main block of code being executed.

def main()
    # You program goes here.
    # The majority of the driving code behind a program is usually found within some sort of main statement. 
    # when you see this: This script can be imported OR run stand alone.
    # Function and Classes in this Module can be reused without the main block of code being executed.
if __name__ == "__main__":    # if dunder name is equal to a string of dunder main. when you see this it's usually followed
    main()                    # by a call to a function named main.
#                             # what it means is if we are not running this program directly don't do it.
