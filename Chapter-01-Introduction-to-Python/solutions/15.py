"""Python Fact Sheet.

This program asks the user for their name, then prints a personalized
Python fact sheet with a matching = border, numbered facts, and a
motivational sign-off.
"""

# Ask the user for their name using input().
user_name = input('Enter your name: ')

# Create a header and a matching border of = characters.
header = 'Python Facts for ' + user_name
border = '=' * len(header)

print(border)
print(header)
print(border)
print()  # blank line after the header

# Print the facts using sep=, end=, and escape sequences.
print('1.', 'Python was created by Guido van Rossum in 1991.', sep='\t', end='\n\n')
print('2.', 'Python uses indentation instead of braces for blocks.', sep='\t', end='\n\n')
print('3.', 'A single Python statement can contain multiple parts using \n escape.', sep='\t', end='\n\n')
print('4.', 'Python supports \t tabs in strings and many useful string methods.', sep='\t', end='\n\n')
print('5.', 'Python is popular in web development, data science, automation, and AI.', sep='\t', end='\n\n')

# Motivational sign-off that uses the user's name.
print('Keep learning Python,', user_name + '!', sep=' ', end='\n')
