#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body
def guess_computer():
	number = random.randint(1, 25)
	count = 1
	print "You have five chances to guess correctly."
	while True and count <= 5:
		user_guess = raw_input(
			"Guess a number between 1 and 25: ")
		try:
			guess_int = int(user_guess)
			if guess_int == number:
				print "Correct!"
				break
			elif count == 5:
				print "You've used up your five chances."
				break
			elif guess_int > 25 or guess_int < 1:
				print "Stick to the rules, please. You're docked a turn."
				count = count + 1  # step up for guesses outside of bounds
			elif guess_int != number:
				if guess_int > number:
					print "Wrong! Try a lower number."
				else: 
					print "Wrong! Try a higher number."
				count = count + 1
		except:
			print "That is not a number, try again." 
			# non-int guesses don't count against them	
	
	print "The computer's number was " + str(number) + "."



################################################################################
def main():


    guess_computer()
    

if __name__ == '__main__':
    main()