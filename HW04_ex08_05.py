#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body
def count(s, l):
	x = 0
	for letter in s:
		if letter == l:
			x = x + 1
	print x



################################################################################
def main():

	count("Whoops!", "o")
	count("Mississippi", "i")
	count("Alabama", "m")
    

if __name__ == '__main__':
    main()