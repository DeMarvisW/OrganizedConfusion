s = input("Do you agree? ")
if s == "Y" or s == "y":
    print("Agreed")
elif s =="N" or s == "n":
    print("Not Agreed")

#Alternatively / Express the same Idea via

s = input("Do you still agree? ")

#if the answer is in the []list provided print Agreed.

if s in ["Y", "y"]:
    print("Agreed")

#if the asnwer in NOT in the []list provided print Not Agreed.

elif s in ["N", "n"]:
    print("Not Agreed")

#Use s.lower method to accept any variation of your response regarding Upper & lower via Object Oriented Programming.

s = input("Do you still agree now? ")
if s.lower() in ["y", "yes"]:
    print("You're Persistant.")
elif s.lower() in ["n", "no"]:
    print("finally you disagree.")

#We can remove the redundancy of 2 s.lower(s) via changing the var "s" to return lower case via.

s = input("what about now? ")
s = s.lower()
if s in ["y", "yes"]:
    print("You're Persistant.")
elif s in ["n", "no"]:
    print("You really don't agree?")
