#                                      Match-Case Statements - Jan 16, 2025

# Match-Case Statements (switch): An Alternative to using many "elif" statements
#                                 Execute some code if a value matches a "case".
#                                 Benefits: Cleaner more readable syntax.
#                                 *New feature added in Python 3.10*  

def day_of_week(day):
    if day == 1:                # We have ONE parameter "day"  
        return "It is Monday."  # Day will be a number 1 - 7 depending on the number, 
    elif day == 2:              # We will return a string corresponding to a day of the week.
        return "It is Tuesday."
    elif day == 3:
        return "It is Wednesday."
    elif day == 4:
        return "It is Thursday."
    elif day == 5:
        return "It is Friday."
    elif day == 6:
        return "It is Saturday."
    elif day == 7:
        return "It is Sunday."
    else:
        return "Not a Valid Day of the week."
    
print(day_of_week(4))
