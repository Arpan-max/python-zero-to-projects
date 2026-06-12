name = input('Enter your name: ')
message = f"Hello, {name}!"
inner_width = len(message) + 4
border = '*' * (inner_width + 2)
blank_line = '*' + ' ' * inner_width + '*'
# center(inner_width) returns a new string of width inner_width.
# It adds spaces before and after message so the text appears centered in that field.
# This method is simple and readable, even if it was not shown in the lecture notes.
message_line = '*' + message.center(inner_width) + '*'
# Alternatively, the manual method computes how much extra space is needed,
# then splits that padding into left and right sides so the message stays centered.
# left uses integer division and right gets any remaining space.
# This is longer, but it shows the centering math explicitly.
# padding = inner_width - len(message)
# left = padding // 2, you will learn this in operators
# right = padding - left
# message_line = '*' + ' ' * left + message + ' ' * right + '*'

print(border)
print(blank_line)
print(message_line)
print(blank_line)
print(border)
