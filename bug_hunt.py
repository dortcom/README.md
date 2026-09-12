# BUG: Missing closing quotation mark at the end of the string. Fixed by adding " before the closing parenthesis.
print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: Typo in the variable name ('nmae' instead of 'name'). Fixed by correcting variable name and formatting string.
print(f"Nice to meet you, {name}")

age = input("How old are you? ")

# BUG: input() returns a string, causing a TypeError when adding 1. Fixed by converting 'age' to an int.
print("Next year you will be " + str(int(age) + 1))