name = input("Enter your full name: ")
age = int(input("Enter your age: "))
height_cm = float(input("Enter your height in cm: "))
python_years = int(input("Enter your years of Python experience: "))

print("Profile Card")
print("Full Name: " + name + " (" + str(type(name)) + ")")
print("Age: " + str(age) + " (" + str(type(age)) + ")")
print("Height (cm): " + str(height_cm) + " (" + str(type(height_cm)) + ")")
print("Python Experience (years): " + str(python_years) + " (" + str(type(python_years)) + ")")

height_m = height_cm / 100.0
print("Height (m): " + str(height_m) + " (" + str(type(height_m)) + ")")
