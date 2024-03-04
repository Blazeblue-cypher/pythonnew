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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first_choice = input("Upon landing on Treasure Island, you encounter a path that goes left and right. Which path do you choose?\n")
if first_choice == "left":
  second_choice = input("Taking the left path leads you to two shovels. One is rusty and the other golden. Which shovel do you pick up?\n")
  if second_choice == "rusty":
    third_choice = input("Upon taking the rusty shovel, three differenet colored Xs appeared. A Blue, Red, and Yellow one. Which do you choose?/n")
    if third_choice == "red":
     print("You walk over to the red X and fall into a pit of fire! GAME OVER!!")
    elif third_choice == "blue":
      print("You walk over to the blue X and fall into a pit full of water and sharks!! GAME OVER!!")
    else:
      print("You walk over to the yellow X, and start to dig and find a chest full of treasure!! YOU WON!!")
  else:  
    print("Upon picking the golden shovel, you turn into a golden statue! GAME OVER!!")
else:
  print("Taking the right path, leads you to an undead Pirate skeleton and it kills you! GAME OVER!!")
