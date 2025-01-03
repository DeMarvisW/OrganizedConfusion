 import random
# print("\u25CF", "\u250C", "\u2500", "\u2510", "\u2502", "\u2514", "\u2518")
# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
# Dictionay of Dice Art observed below: Each key is a value, each value is a tuplemade of strings, 
dice_art = {
   1: ("┌─────────┐", 
       "│         │", 
       "│    ●    │", 
       "│         │", 
       "└─────────┘"), 
   2: ("┌─────────┐", 
       "│         │", 
       "│  ●   ●  │", 
       "│         │", 
       "└─────────┘"),
   3: ("┌─────────┐", 
       "│ ●       │", 
       "│    ●    │", 
       "│       ● │", 
       "└─────────┘"),  
   4: ("┌─────────┐", 
       "│ ●     ● │", 
       "│         │", 
       "│ ●     ● │", 
       "└─────────┘"),         
   5: ("┌─────────┐", 
       "│ ●     ● │", 
       "│    ●    │", 
       "│ ●     ● │", 
       "└─────────┘"), 
   6: ("┌─────────┐", 
       "│ ●     ● │", 
       "│ ●     ● │", 
       "│ ●     ● │", 
       "└─────────┘") 
       }
#Creat a list of dice
dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total += die
print(f"total: {total}")

# We can print the dice side by side via:#51-53 
# then 
#55 for line in range(5):
#56      for die in dice:
#57          print(dice_art.get(die)[line], end="")
#58      print() 
#59
#60 for die in dice:
#61      total += die
#62 print(f"total: {total}")
