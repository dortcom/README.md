# BUG: Missing closing quote on the string string literal. Fixed by adding a quote after "Hunt!".
print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: Typo in variable name ('nmae' instead of 'name'). Fixed spelling and converted to an f-string.
print(f"Nice to meet you, {name}")

age = input("How old are you? ")

# BUG: input() returns a string, causing a TypeError when adding 1. Fixed by converting age with int().
print("Next year you will be " + str(int(age) + 1))
