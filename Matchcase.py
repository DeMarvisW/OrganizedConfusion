#                                      Match-Case Statements - Jan 16, 2025

# Match-Case Statements (switch): An Alternative to using many "elif" statements
#                                 Execute some code if a value matches a "case".
#                                 Benefits: Cleaner more readable syntax.
#                                 *New feature added in Python 3.10*  


# def day_of_week(day):
#     if day == 1:                       # We have ONE parameter "day" 
#         return "It's Monday."          # Day will be a number 1 - 7 depending on the number,
#     elif day == 2:                     # We will return a string corresponding to a day of the week.
#         return "it's Tuesday."
#     elif day == 3:
#         return "it's Wednesday."
#     elif day == 4:
#         return "it's Thursday."
#      elif day == 5:
#         return "it's Friday"
#     elif day == 6:
#         return "it's Saturday."
#     elif day == 7:
#         return "it's Sunday."
#     else:
#         return "Not a valid day of the week!"

# print(day_of_week(4))                      # Returns the string "It's Thursday."



# def day_of_week(day):
#     match day:
#         case 1:                                  # As an alternative you can take your if and elif statements
#             return "It is Monday."               # and isntead inclose them w/in a match - case.
#         case 2:                                  # The CASE will be the value we're examining (day).
#             return "It is Tuesday."              # Replacing the IF statement "If day ==" with "CASE"
#         case 3:                                  # If you have an else clause it will be replace with "CASE _" (case blank)
#             return "It is Wednesday."            # * The underscore_ is a wildcard. 
#         case 4:                                  # It states we will perform this case if there are no matching cases.
#             return "It is Thursday."
#         case 5:
#             return "It is Friday."
#         case 6:
#             return "It is Saturday."
#         case 7:
#             return "It is Sunday."
#         case _:
#             return "Not a Valid Day of the week."
    
# print(day_of_week(4))

# def is_weekend(day):
#     match day:
#         case "Monday":                      
#             return False                    
#         case "tuesday":
#             return False
#         case "Wednesday":
#             return False
#         case "Thursday":
#             return False
#         case "Friday":
#             return False
#         case "Saturday":
#             return True
#         case "Sunday":
#             return True
#         case _:
#             return False
        
# print(is_weekend("Sunday"))


#                                    In order to not repeat ourself soo much we can use the OR logical operator.
#                                    | = "Or Logical Operator"


def is_weekend(day):
     match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
               return False
        case "Saturday" | "Sunday":
               return True
           
        case _:
                return False

print(is_weekend("Sunday"))
