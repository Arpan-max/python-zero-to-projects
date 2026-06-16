# Ask the user to enter two decimal numbers and cast both inputs to float immediately.
num1 = float(input("Enter the first decimal number: "))
num2 = float(input("Enter the second decimal number: "))

result = num1 + num2
print(f"{num1} + {num2} = {result}")

# Without casting, input() returns strings, and the + operator would concatenate instead of add.
# For example:
#    first = input("Enter the first decimal number: ")
#    second = input("Enter the second decimal number: ")
#    print(first + second)  # e.g. "1.2" + "3.4" -> "1.23.4"