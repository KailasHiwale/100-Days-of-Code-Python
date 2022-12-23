# Project 3: Tresure island Game
"""
Your mission is to find the treasure.

Flow 1:
Which side you want to go? Left or Right? right
Ohh you fell down to river.. Game Over.

Flow 2: 
Which side you want to go? Left or Right? left
Good!! You've came near. How would you like Swim or Wait? swim
Ohh you get drawn.. Game Over.

Flow 3:
Which side you want to go? Left or Right? left
Good!! You've came near. How would you like Swim or Wait? wait
Great!! You've reached to the Tresure Island. Which door you would like to enter ? Red, Yellow, Blue? yellow
Awesome!! You Win!

Flow 4:
Which side you want to go? Left or Right? left
Good!! You've came near. How would you like Swim or Wait? wait
Great!! You've reached to the Tresure Island. Which door you would like to enter ? Red, Yellow, Blue? red
OMG you got trapped. Game Over.

Flowchart link -
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

side = input("Which side you want to go? Left or Right? ")
if side.lower() == "right":
    print("Ohh you fell down to river.. Game Over.")
else:
    going_by = input("Good!! You've came near. How would you like Swim or Wait? ") 
    if going_by.lower() == "swim":
        print("Ohh you get drawn.. Game Over.")
    else:
        door = input("Great!! You've reached to the Tresure Island. Which door you would like to enter ? Red, Yellow, Blue? ")
        if door.lower() == "yellow":
            print("Awesome!! You Win!")
        else:
            print("OMG you got trapped. Game Over.")