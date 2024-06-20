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
print("---------------WELCOME TO TREASURE ISLAND---------------.")
print("...........Your mission is to find the treasure............")
choice = input("You are at croassroad where you want to go,Type 'left' or 'right':\n")
if choice.lower() == "right" : 
    print("You fell into hole \n GAME OVER!!")
elif choice.lower() == "left" : 
    print("You have came to an lake.There is an island in the middle of lake")
choice1 = input("You can 'swim' across the lake or you can 'wait' for the boat:\n")
if choice1.lower() == "swim": 
    print("You got attacked by trout\nGAME OVER!!")
elif choice1.lower() == "wait" : 
    print("You have come to island unharmed.")
choice2 = input("There are three doors at main entrance of island which leads to an castle,\nFirst door is 'red',\nSecond door is 'blue'\nThird door 'yellow'\nChoose the correct door and find your way to treasure room!!\n")
if choice2.lower() == "red" : 
    print("You got burned by fire\nGAME OVER!!")
elif choice2.lower() == "blue" : 
    print("Eaten by beast..\nGAME OVER!!")
else : 
    choice2.lower() == "yelllow"
    print("You succesfully came to the treasure room\nThere is big dragon waiting you for there\nHe ask you riddle?\nWhat has keys but can't open locks?")
choice3 = input("")
if choice3.lower() == "piano" : 
    print("This treasure is yours\n----------YOU WON THE GAME----------")
else : 
    choice3 == "I dont know the answer"
    print("You became the dragon food..\nGAME OVER!!")