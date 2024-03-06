import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5 #to get any floating # before 5
print(random_float)

lucky_number= random.randint(1, 100)
print(f"Your lucky number is {lucky_number}")

coin_toss = random.randint(0,1)
if coin_toss == 1:
  print("Heads")
else:
  print("Tails")
  