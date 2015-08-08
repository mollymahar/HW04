# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function

def rotate_word(s, offset):
	new_string = ''
	new_letter = ''
	for char in s:
		# Have to offset correctly for capital letters and lowercase since there
		# are other characters in between in ASCII numeric representation.

		x = ord(char) + offset
		if 65 <= ord(char) <= 90: 				# uppercase letters
			if 65 <= x <= 90:
				new_letter = chr(x)
			elif x > 90: 						#if it's now greater than Z
				new_letter = chr(65 + (x - 91))
				# at ascii 91 loop back down to 65 and count up
			elif x < 65: 						#if it's now less than A
				new_letter = chr(90 - (64 - x))
				# at ascii 64 loop back up to 90 and count down

		elif 97 <= ord(char) <= 122: 			#lowercase letters
			if 97 <= x <= 122:
				new_letter = chr(x)
			elif x > 122: 						#if it's now greater than z	
				new_letter = chr(97 + (x - 123))
				# at ascii 123 loop back down to 97 and count up
			elif x < 97: 						#if it's now less than a
				new_letter = chr(122 - (96 - x))
				# at ascii 96 loop back up to 122 and count down

		new_string = new_string + new_letter

	print new_string
	return new_string




def main():
	rotate_word("cheer", 7)
	rotate_word("melon", -10)
	rotate_word("cheer", 13)
	rotate_word("OUTPUT", 13)

if __name__ == '__main__':
	main()