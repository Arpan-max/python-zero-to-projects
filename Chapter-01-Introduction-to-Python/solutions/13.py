# Use a raw string for the ASCII art so backslashes stay backslashes.
# Without the leading r, Python treats sequences like \n, \t, or an escaped quote
# inside the string. That can change the text and break the picture.
# The raw string means "do not interpret backslashes as escape characters".
art = r'''
       /\
      /  \
     /----\
    /      \
   /  /\    \
  /__/  \____\
  |  []  []  |
  |   ____   |
  |__|    |__|
'''

print(art)
