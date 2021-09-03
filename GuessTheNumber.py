# Guess my nbr
from random import randint
nbr_essays_max = 5
nbr_essays = 1
max_random = 20
my_nbr = randint(1,max_random) # number chosen by the PC
your_nbr = 0 # Number proposed by the player
print("I chose a number between 1 and",max_random)
print("It's up to you to guess it in ",nbr_essays_max,"attempts at most!")
while your_nbr != my_nbr and nbr_essays <= nbr_essays_max:
 print("Essay nbr ",nbr_essays)

 while True:
  try:
   your_nbr = int(input("Your proposition : "))
   break
  except ValueError:
   print("Invalid response. Try again !")

 if your_nbr < my_nbr:
  print("Too small")
 elif your_nbr > my_nbr:
  print("Too big")
 else:
  print("Good Job ! You found ", my_nbr, "in", nbr_essays, "essay(s)")

 nbr_essays += 1

 if nbr_essays > nbr_essays_max and your_nbr != my_nbr:
  print("Sorry, you used your", nbr_essays_max, "essays to no avail")
  print("I had chosen the number", my_nbr, ".")




