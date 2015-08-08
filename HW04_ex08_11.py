#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """This function only checks whether the string's first character is 
        lowercase. This could be better served by having a break statement 
        after the return True, and then have the return False outside the 
        for loop. As is, it will only run through the first letter and 
        either return True or False.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """This doesn't actually use the variable c, but rather creates a new
        string to test that is 'c'. It will always be True b/c it is lowercase.
        Also it returns a string rather than a boolean, so depending what your
        purpose is, that could present a problem.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """flag will just end up being the last character of the string, so it
        won't actually tell you if any other letters are lowercase in the string.
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """This one works, because it uses the or statement. So as soon as it's
        True, it stays True, and returns that value.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """This one is saying 'if not True, return False, otherwise return True.'
        It's not working with spaces, since they're not lowercase. When it hits
        a space, it returns False. It also returns false at the first uppercase
        letter.
    """
    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    any_lowercase1("CAPS in the beginning")
    any_lowercase2("Cats")
    any_lowercase3("capital letter at the enD")
    any_lowercase5("TRYthis")
    

if __name__ == '__main__':
    main()