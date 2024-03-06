import random

pokemon = ["charmander", "squirtle", "bulbasaur"]

trainer_choice = int(input("Chose your pokemon. Enter 0 for charmander, 2 for squirtle, or 3 for bulbasaur\n"))
print("I chose you!")
print(pokemon[trainer_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(pokemon[computer_choice])

if trainer_choice == 0 and computer_choice == 2:
  print("You won!")
elif trainer_choice == 0 and computer_choice == 1:
  print("You lose!")
elif trainer_choice == 1 and computer_choice == 0:
  print("You won!")
elif trainer_choice == 1 and computer_choice == 2:
  print("You lose!")
elif trainer_choice == 2 and computer_choice == 0:
  print("You won!")
elif trainer_choice == 2 and computer_choice == 1:
  print("You lost!")
elif trainer_choice == computer_choice:
  print("It's a draw")