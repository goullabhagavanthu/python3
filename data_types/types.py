# literal assignments
first = "goulla"
last =  "bhagavanthu"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))   

# Concatenation
# fullname = first + " " + last
# print(fullname)

# fullname += "!"
# print(fullname)

# Casting a number to string
# decade = str(1960)
# print(type(decade))
# print(decade)

# statement = "I like the music from the " + decade + "s."
# print(statement)

# String Methods

# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# Build a menu 
# title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + "$1".rjust(4))
# print("Muffin".ljust(16, ".") + "$2".rjust(4))
# print("Cheesecake".ljust(16, ".") + "$3".rjust(4))

# print("")

# string index values
# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:]) 

# Some Methods return boolean data
# print(first.startswith("D"))
# print(first.endswith("Z"))

# Boolean data types
# myvalue =  True
# x = bool(False)
# print(isinstance(myvalue, bool)) 

# Numeric data types

# integer type
# price = 100
# best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int)) 

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa)) 

# Complex type
# comp_value = 5 + 3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag) 

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))

import math
print(math.pi)
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "500088"
zip_value = int(zipcode)
print(type(zip_value))
