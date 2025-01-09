# Dictionary =  a collection of {key:value} pairs.
#               Ordered and changeable Duplicates not allowed / possible.
#                Traditional Dictionary Comparison: 
#                 Key = Word   Value =  Definition 


capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#                                              dir()

# print(dir(capitials)): To review different attributes and methods of a dictionary.

#                                              help()

# print(help(capitals)): To see an in depth description of all of the attributes and methods.

#                                             .get()

# print(capitals.get("USA")):   To "get" one of the values from the dictionary. You woudld "get" the "key"
# Would return "None" if key / value is NOT located within our dictionary.
# print(capitals.get("Japan"))
# print(capitals.get("India"))


#                                           If Statement

# Can use within an "IF" statement:

# if capitals.get("USA"):             # Using a "Key" if a value is returned then we will print a custom string / statement. 
#    print("That Capital Exist!")
# else:                               #Using a "Key" if a value is not returned then we will print a custom string / statement.
#     print("That Capital does NOT exist!")

#                                             .update()

# We can update our dictionary to include additional data via the Update method OR Change one of the existing key/value pairs.

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Texas"})

# Upon printing our Dictionary. The new data will be observed.


#                                               .pop()

# To remove a key:Value pair you can utilize the .pop method
# capitals.pop("China")
# China is now observed as removed from the dictionary.


#                                              .popitem()

# Remove the latest / last key:value pair by using the "popitem()" method.
# capitals.popitem()
# With the popitem() method there is no need to pass in a key into the ().
# The last data set is now observed as removed from the dictioanary.


#                                              .clear

# Clears the attached Dictionary's contents

#                                              .keys()

# Gets all of the keys within the dictionary but NOT the values. 

# keys = capitals.keys()           
# for key in capitals.keys:
#   print(key)


#                                              .values()

# Get every value within your dictionary.

# values = capitals.values()
# for value in capitals.values():
#    print(value)


#                                              .items()

# items = capitals.items()
for key, value in capitals.items():
    print(f"{key}, {value}")
