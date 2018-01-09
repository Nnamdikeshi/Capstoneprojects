# Import our random module
import random

# Assign our randomly generated int to a variable
guess_me = (random.randint(0,9))

# Gather only integer user input
user_guess = int(input("Guess the number i am thinking of..."))

# If user guess is less-than random int then print..
if user_guess < guess_me:
	print ("Too low")
	
# If user guess is greater-than random int then print..
if user_guess > guess_me:
	print ("Too High")
	
# If user guess is equal to random int then print..
if user_guess == guess_me:
	print ("Correct!")