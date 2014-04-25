#Guess the number game
#Z0MBiE 2014

import random
number = random.randint(1,20)
guess = -1

while (guess != number):
	guess = int(input("Guess the number: "))

	if guess == number:
		print("You got it!")
	elif guess < number:
		print("The number is bigger than that.")
	elif guess > number:
		print("The number is smaller than that.")