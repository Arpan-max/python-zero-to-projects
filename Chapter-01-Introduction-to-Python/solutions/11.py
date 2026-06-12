item1_name = "Python Book"
item1_price = 499
item2_name = "USB Cable"
item2_price = 199
item3_name = "Notebook"
item3_price = 79
item4_name = "Pen (2x)"
item4_price = 40

total = item1_price + item2_price + item3_price + item4_price

print()
print("  ================================")
print()
print("  PYTHON SHOP - RECEIPT")
print()
print("  ================================")
print()
print("  Item              Price")
print("  --------------------------------")
# Use fixed spaces after each item name so the Rs. column stays aligned.
print("  " + item1_name + "      Rs. " + str(item1_price))
print("  " + item2_name + "        Rs. " + str(item2_price))
print("  " + item3_name + "         Rs. " + str(item3_price))
print("  " + item4_name + "         Rs. " + str(item4_price))
print("  --------------------------------")
print("  TOTAL            Rs. " + str(total))
print()
print("  ================================")
print()
print("  Thank you for shopping with us!")
