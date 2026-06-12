name = input('Enter your name: ')
language = input('Favourite language: ')
# Using f-string (formatted string literal) to embed variables directly into the string
# The f prefix allows us to use {variable_name} syntax to insert values
print(f'Hey {name}! Great choice - {language} is amazing!')

# Alternative without f-string: using the + operator to concatenate strings
# print('Hey ' + name + '! Great choice - ' + language + ' is amazing!')
