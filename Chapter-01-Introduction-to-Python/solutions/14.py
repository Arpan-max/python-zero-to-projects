"""Bug Hunt solution for Chapter 01, Practice Set question 14.

This file fixes the 6 deliberate bugs from the buggy sample program.
The corrected program runs successfully and prints a greeting.
"""

# Bug 1: Print() should be lowercase print()
# Bug 2: The first print string was missing a closing quote
# Bug 3: Input() should be lowercase input()
# Bug 4: Variable name mismatch: userName vs user_name
# Bug 5: Len should be lowercase len() and the print call needs commas
# Bug 6: Goodbye line should not be commented out

print('Welcome to Python!')
user_name = input('What is your name? ')
print('Hello ' + user_name + '!')
print('Name has', len(user_name), 'chars.')
print('Goodbye ' + user_name + '!')
