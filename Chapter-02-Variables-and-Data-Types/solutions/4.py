source = "7"

int_value = int(source)
float_value = float(source)
str_value = str(int_value)

print("source:", source, "type:", type(source))
print("int_value:", int_value, "type:", type(int_value))
print("float_value:", float_value, "type:", type(float_value))
print("str_value:", str_value, "type:", type(str_value))

# The following line would raise a ValueError because "abc" cannot be converted to an integer:
# ValueError: invalid literal for int() with base 10: 'abc'
# invalid_int = int("abc")
