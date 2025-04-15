# Task 1:Basic Mathematical Operations

# two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#basic mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Display the results
print("\nResults:")
print(f"Addition:  {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication:{multiplication}")
print(f"Division:{division}")



# Task 2: Create a Personalized Greeting

# first and last name as input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Concatenate into full name
full_name = f"{first_name} {last_name}"

# Print personalized greeting
print(f"\nHello, {full_name}! Welcome to the program. Have a great day!")
