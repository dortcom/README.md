# Ask the user for their age and convert it to an integer
age = int(input("Please enter your age: "))

# Store the Boolean result evaluating if the user is 18 or older
is_adult = age >= 18

# Display the Boolean value directly
print("Is adult:", is_adult)

# Use conditional logic to determine ticket price
if is_adult:
    print("Ticket Price: Full Adult Fare - $15.00")
else:
    print("Ticket Price: Discounted Child Fare - $8.00")