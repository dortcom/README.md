# Ask the user for their full name
full_name = input("Please enter your full name: ")

# Split the string into a list using spaces as dividers
name_parts = full_name.split()

# Check how many name parts were entered
if len(name_parts) >= 2:
    # Greet using the first name (index 0)
    print(f"Hello, {name_parts[0]}! Great to meet you.")
else:
    # Prompt for a full name if only one word was provided
    print("Please provide both your first and last name next time!")