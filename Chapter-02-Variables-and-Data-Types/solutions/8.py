# Version 1: keep the inputs as strings and concatenate them
# The `input()` function returns a string, so using + on two strings
# produces a string concatenation, not a numeric sum.
first_number = input("Enter the first whole number: ")
second_number = input("Enter the second whole number: ")
print("String sum:", first_number + second_number)

# Version 2: cast the inputs to int and compute the real arithmetic sum
# Converting the strings to integers allows Python to add their numeric values.
first_number_int = int(first_number)
second_number_int = int(second_number)
print("Numeric sum:", first_number_int + second_number_int)
