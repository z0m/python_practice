#Guess the number game
#Z0MBiE 2014

import random
number = random.randint(1,20)
guess = -1
count = 0

while (guess != number):
	guess = int(input("Guess the number: "))
	count = count + 1
	if guess == number:
		print("You got it!")
	elif guess < number:
		print("The number is bigger than that.")
	elif guess > number:
		print("The number is smaller than that.")
if count > 3:
	print("That must have been tough.")
else:
	print("That was quick!")